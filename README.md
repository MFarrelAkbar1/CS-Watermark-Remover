# CS Watermark Remover

Hapus watermark CamScanner dari file PDF.

## Fitur

- Hapus watermark image di footer
- Hapus teks "CamScanner" dan "Dipindai dengan CamScanner"
- Deteksi otomatis posisi watermark
- Clean metadata
- Save ke file baru (_cleaned.pdf)

## Install

Install PyMuPDF:
```bash
pip install pymupdf
```

## Usage

```bash
python remove_camscanner.py scan.pdf
```

Atau dengan full path:
```bash
python remove_camscanner.py "C:\Documents\scan.pdf"
```

## Output

```
Membuka: scan.pdf
Memproses 6 halaman...
  Hal 1: 1 img, 0 txt
  Hal 2: 1 img, 0 txt
  ...
Cleaning metadata...
Saving: scan_cleaned.pdf

Done!
Pages: 6
Images removed: 6
Text removed: 0
Output: scan_cleaned.pdf
```

## Notes

- File asli tidak diubah, output saved ke `*_cleaned.pdf`
- Metadata Producer/Creator dibersihkan
- Watermark dihapus permanen (redacted)

## Troubleshooting

Error `No module named 'fitz'`:
```bash
pip install pymupdf
```

Error `Permission denied` - tutup PDF reader dulu.

## Requirements

- Python 3.7+
- PyMuPDF
