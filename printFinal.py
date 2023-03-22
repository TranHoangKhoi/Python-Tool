import win32print
import win32ui
import win32con
import win32
from PIL import Image


# Thiết lập các thuộc tính cho tài liệu
printer_name = win32print.GetDefaultPrinter()
print(printer_name)
hprinter = win32print.OpenPrinter(printer_name)
devmode = win32print.GetPrinter(hprinter, 2)["pDevMode"]
devmode.PaperSize = 9  # A4
devmode.Color = 1  # in màu

# Tạo PyCDC và cài đặt thiết lập in
hdc = win32ui.CreateDC()
hdc.CreatePrinterDC(printer_name)

# In tài liệu
hdc.StartDoc("Test document")
hdc.StartPage()

# Gửi dữ liệu in tới printer
# text = "Tao tét lần thứ 77"
# hdc.TextOut(10, 10, text)
doc = open("text2.txt", 'r').readlines()
for i, text in enumerate(doc):
    print(i, text)
    hdc.TextOut(0, i*50, text)
    hdc.MoveTo(0, i*50)

# Kết thúc tài liệu và đóng printer handle
hdc.EndPage()
hdc.EndDoc()
hdc.DeleteDC()
win32print.ClosePrinter(hprinter)
