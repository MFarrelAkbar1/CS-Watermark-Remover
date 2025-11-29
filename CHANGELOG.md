# Changelog

## Version 2.0 (2025-11-28)

### ✨ Fitur Baru
- **Image Watermark Removal**: Menghapus watermark berbentuk image/graphic di footer
  - Deteksi otomatis watermark "🔒 Dipindai dengan CamScanner" di pojok kanan bawah
  - Menghapus logo CS dan teks watermark yang di-embed sebagai gambar
  - Algoritma deteksi berdasarkan posisi (bottom area, right side, small size)
  - Support deteksi spesifik untuk posisi CamScanner standard (364, 807, 585, 832)

### 🔧 Perbaikan
- **Encoding Fix**: UTF-8 encoding otomatis untuk Windows Console
  - Emoji sekarang muncul dengan benar di Command Prompt
  - Tidak ada lagi UnicodeEncodeError di Windows
- **Fill Parameter Fix**: Menggunakan list `[1, 1, 1]` instead of tuple untuk PyMuPDF 1.26.6+
- **Redaction Count Fix**: Increment counter yang benar (1 per instance, bukan len(instances))

### 📊 Peningkatan
- Output statistics sekarang menampilkan image dan text watermark terpisah
- Traceback detail untuk error debugging
- Better progress reporting per halaman

### 🧪 Testing
- Tested pada scan.pdf (6 halaman) - berhasil menghapus 6 image watermarks
- Tested pada test_document.pdf (3 halaman) - berhasil menghapus text watermarks
- Verified output PDF tidak memiliki watermark

### 📝 Dokumentasi
- Update README.md dengan fitur v2.0
- Update QUICK_START.txt dengan info image watermark removal
- Tambah analyze_pdf.py untuk debugging watermark detection

## Version 1.0 (Initial Release)

### ✨ Fitur
- Text watermark removal (case-insensitive search)
- Metadata cleaning (Producer/Creator)
- File optimization (garbage collection, deflate)
- Error handling (file not found, permission error, invalid PDF)

### 📁 Files
- remove_camscanner.py - Main script
- create_test_pdf.py - Test PDF generator
- requirements.txt - Dependencies
- README.md - Documentation
- run_example.bat - Windows batch script
