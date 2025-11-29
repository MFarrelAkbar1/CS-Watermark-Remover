#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import fitz

def clean_camscanner_pdf(input_path):
    try:
        if not os.path.exists(input_path):
            print(f"Error: File tidak ditemukan: {input_path}")
            return None, None

        if not input_path.lower().endswith('.pdf'):
            print(f"Error: Bukan file PDF: {input_path}")
            return None, None

        print(f"Membuka: {os.path.basename(input_path)}")
        doc = fitz.open(input_path)

        total_pages = len(doc)
        img_removed = 0
        txt_removed = 0

        print(f"Memproses {total_pages} halaman...")

        for page_num in range(total_pages):
            page = doc[page_num]
            page_img = 0
            page_txt = 0

            search_terms = ["CamScanner", "camscanner", "CAMSCANNER", "Dipindai dengan", "Scanned by"]
            for term in search_terms:
                for inst in page.search_for(term):
                    page.add_redact_annot(inst, fill=[1, 1, 1])
                    page_txt += 1

            if page_txt > 0:
                page.apply_redactions()

            rect = page.rect
            h = rect.height
            w = rect.width

            for img in page.get_images():
                xref = img[0]
                for img_rect in page.get_image_rects(xref):
                    bottom = img_rect.y0 > h * 0.8
                    small = (img_rect.x1 - img_rect.x0) < w * 0.4
                    right = img_rect.x0 > w * 0.5

                    camscanner_pos = (img_rect.x0 > 300 and img_rect.y0 > 780 and
                                     img_rect.y1 < 842 and img_rect.x1 < 600)

                    if (bottom and small and right) or camscanner_pos:
                        exp = fitz.Rect(img_rect.x0-2, img_rect.y0-2, img_rect.x1+2, img_rect.y1+2)
                        page.add_redact_annot(exp, fill=[1, 1, 1])
                        page_img += 1

            if page_img > 0:
                page.apply_redactions()

            if page_img > 0 or page_txt > 0:
                print(f"  Hal {page_num+1}: {page_img} img, {page_txt} txt")

            img_removed += page_img
            txt_removed += page_txt

        print("Cleaning metadata...")
        meta = doc.metadata
        old_prod = meta.get('producer', '')
        old_creator = meta.get('creator', '')

        doc.set_metadata({
            'producer': 'PDF Cleaner',
            'creator': 'PDF Cleaner',
            'title': meta.get('title', ''),
            'author': meta.get('author', ''),
            'subject': meta.get('subject', ''),
        })

        output = f"{os.path.splitext(input_path)[0]}_cleaned.pdf"

        print(f"Saving: {os.path.basename(output)}")
        doc.save(output, garbage=4, deflate=True, clean=True)
        doc.close()

        return output, {
            'pages': total_pages,
            'img': img_removed,
            'txt': txt_removed,
            'old_prod': old_prod,
            'old_creator': old_creator,
            'output': output
        }

    except PermissionError:
        print(f"Error: Permission denied - {input_path}")
        return None, None
    except fitz.FileDataError:
        print(f"Error: Invalid PDF - {input_path}")
        return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

def main():
    print("CamScanner Watermark Remover v2.0\n")

    if len(sys.argv) < 2:
        print("Usage: python remove_camscanner.py <pdf_file>")
        print('Example: python remove_camscanner.py "scan.pdf"')
        sys.exit(1)

    output, stats = clean_camscanner_pdf(sys.argv[1])

    if output and stats:
        print("\nDone!")
        print(f"Pages: {stats['pages']}")
        print(f"Images removed: {stats['img']}")
        print(f"Text removed: {stats['txt']}")
        if stats['old_prod']:
            print(f"Old producer: {stats['old_prod']}")
        print(f"Output: {stats['output']}")
    else:
        print("\nFailed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
