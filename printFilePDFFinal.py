import win32api
import win32print

GHOSTSCRIPT_PATH = r"E:\xamp\htdocs\AME\AME-1230-UPDATE-TOOL\GHOSTSCRIPT\bin\gswin32.exe"
GSPRINT_PATH = r"E:\xamp\htdocs\AME\AME-1230-UPDATE-TOOL\GSPRINT\gsprint.exe"

# YOU CAN PUT HERE THE NAME OF YOUR SPECIFIC PRINTER INSTEAD OF DEFAULT
currentprinter = win32print.GetDefaultPrinter()

win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "' +
                      GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "createPDFLabel.pdf"', '.', 0)
