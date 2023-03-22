from flask import Flask
import win32print
import win32ui
import win32api
import win32print


app = Flask(__name__)

GHOSTSCRIPT_PATH = "./GHOSTSCRIPT/bin/gswin32.exe"
GSPRINT_PATH = "./GSPRINT/gsprint.exe"

currentprinter = win32print.GetDefaultPrinter()


@app.route('/')
def root():
    return "Home page"


@app.route('/hello')
def hello_world():

    win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "' +
                          GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "createPDF.pdf"', '.', 0)

    return "Done!"


if __name__ == '__main__':
    app.run()
