#!/usr/bin/env python3
import sys
import os

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import fitz

def analyze_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    print(f"Analyzing: {pdf_path}")
    print(f"Total pages: {len(doc)}\n")

    for page_num in range(len(doc)):
        page = doc[page_num]
        print(f"=== Page {page_num + 1} ===")

        rect = page.rect
        print(f"Size: {rect.width} x {rect.height}")

        text = page.get_text()
        if "camscanner" in text.lower() or "dipindai" in text.lower():
            print(f"Found CamScanner text")
            areas = page.search_for("CamScanner")
            areas.extend(page.search_for("Dipindai"))
            for area in areas:
                print(f"  {area}")

        imgs = page.get_images()
        print(f"Images: {len(imgs)}")

        for i, img in enumerate(imgs):
            xref = img[0]
            print(f"  Img {i+1}: xref={xref}")
            for r in page.get_image_rects(xref):
                print(f"    Pos: {r}")
                if r.y1 > rect.height * 0.85:
                    print(f"    Footer area - likely watermark")

        print(f"Vectors: {len(page.get_drawings())}")
        print()

    doc.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_pdf.py <pdf_file>")
        sys.exit(1)

    analyze_pdf(sys.argv[1])
