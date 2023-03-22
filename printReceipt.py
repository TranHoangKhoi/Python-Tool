import win32api
import win32print

# Mở tệp tin biên lai
file_path = "./receipt.py"
file = open(file_path, "r")

# Lấy nội dung và chuyển đổi nó thành chuỗi byte
file_content = file.read()
content_bytes = bytes(file_content, 'utf-8')

# Lấy tên máy in mặc định
printer_name = win32print.GetDefaultPrinter()

# Mở máy in và in nội dung của biên lai
hPrinter = win32print.OpenPrinter(printer_name)
try:
    hJob = win32print.StartDocPrinter(hPrinter, 1, ("Biên lai", None, "RAW"))
    try:
        win32print.StartPagePrinter(hPrinter)
        win32print.WritePrinter(hPrinter, content_bytes)
        win32print.EndPagePrinter(hPrinter)
    finally:
        win32print.EndDocPrinter(hPrinter)
finally:
    win32print.ClosePrinter(hPrinter)
