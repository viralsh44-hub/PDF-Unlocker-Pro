from src.gui import PDFUnlockerGUI
from src.unlock_engine import UnlockEngine

engine = UnlockEngine()

pdfs = engine.scan_pdf_folder("D:/TestPDF")

print(pdfs)

def main():

    app = PDFUnlockerGUI()

    app.run()


if __name__ == "__main__":
    main()