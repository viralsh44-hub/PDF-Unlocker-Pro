from pathlib import Path


class UnlockEngine:

    def __init__(self):
        pass

    def scan_pdf_folder(self, folder_path):

        folder = Path(folder_path)

        if not folder.exists():
            return []

        pdf_files = sorted(folder.glob("*.pdf"))

        return pdf_files