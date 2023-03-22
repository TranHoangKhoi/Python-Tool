import os
import tempfile
import win32print
from PIL import Image

# Đường dẫn đến file ảnh
duong_dan_anh = "E:/xamp/htdocs/AME/AME-1230-UPDATE/1230logo.png"

# Tên máy in (hoặc tên địa chỉ IP nếu kết nối qua wifi)
ten_mayin = win32print.GetDefaultPrinter()
print(ten_mayin)

# Mở file ảnh và chuyển sang định dạng BMP
with Image.open(duong_dan_anh) as img:
    temp_file_path = os.path.join(tempfile.gettempdir(), "temp_image.bmp")
    img.convert(mode="1").save(temp_file_path, "BMP")

# Lấy thông tin về máy in
printer_info = None
for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_CONNECTIONS + win32print.PRINTER_ENUM_LOCAL):
    if printer[2] == ten_mayin:
        printer_info = printer
        break
if not printer_info:
    raise RuntimeError(f"Không tìm thấy máy in với tên {ten_mayin}")

# In tài liệu
hPrinter = win32print.OpenPrinter(printer_info[2])
try:
    # Bắt đầu in
    hJob = win32print.StartDocPrinter(
        hPrinter, 1, ("Hình ảnh in", None, "RAW"))
    try:
        # Bắt đầu trang in
        win32print.StartPagePrinter(hPrinter)
        try:
            # Đọc file ảnh và in từng dòng dữ liệu theo trình tự
            with open(temp_file_path, "rb") as f:
                while True:
                    data = f.read(4096)
                    if not data:
                        break
                    win32print.WritePrinter(hPrinter, data)
        finally:
            # Kết thúc trang in
            win32print.EndPagePrinter(hPrinter)
    finally:
        # Kết thúc in
        win32print.EndDocPrinter(hPrinter)
finally:
    win32print.ClosePrinter(hPrinter)
