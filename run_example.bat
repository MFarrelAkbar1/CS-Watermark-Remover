@echo off
REM Contoh batch script untuk menjalankan CamScanner Remover di Windows
REM Edit path di bawah sesuai dengan lokasi file PDF Anda

echo ========================================
echo CamScanner Watermark Remover
echo ========================================
echo.

REM Ganti path ini dengan path file PDF Anda
set PDF_FILE="C:\Users\HP VICTUS\Documents\sample.pdf"

REM Atau gunakan argument dari drag-and-drop
if not "%~1"=="" set PDF_FILE="%~1"

echo Memproses file: %PDF_FILE%
echo.

python remove_camscanner.py %PDF_FILE%

echo.
echo ========================================
pause
