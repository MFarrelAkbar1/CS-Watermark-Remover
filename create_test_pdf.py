#!/usr/bin/env python3
import fitz

def create_test_pdf():
    doc = fitz.open()

    for i in range(3):
        page = doc.new_page(width=595, height=842)
        text = f"Halaman {i + 1}\n\nIni adalah dokumen test."
        page.insert_text((100, 100), text, fontsize=14)

        if i == 0:
            page.insert_text((200, 800), "Scanned by CamScanner", fontsize=8, color=(0.5, 0.5, 0.5))
        elif i == 1:
            page.insert_text((150, 30), "CamScanner", fontsize=10, color=(0.7, 0.7, 0.7))
        else:
            page.insert_text((50, 50), "camscanner", fontsize=8, color=(0.6, 0.6, 0.6))
            page.insert_text((400, 750), "CAMSCANNER", fontsize=8, color=(0.6, 0.6, 0.6))

    doc.set_metadata({
        'producer': 'CamScanner',
        'creator': 'CamScanner App',
        'title': 'Test Document',
        'author': 'Test User'
    })

    output = "test_document.pdf"
    doc.save(output)
    doc.close()

    print(f"Created: {output}")
    print("3 pages with CamScanner watermarks")
    print(f"\nRun: python remove_camscanner.py \"{output}\"")

if __name__ == "__main__":
    create_test_pdf()
