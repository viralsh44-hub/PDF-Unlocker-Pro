from pathlib import Path
from datetime import datetime


class ReportGenerator:

    def __init__(self):
        self.report_folder = Path("reports")
        self.report_folder.mkdir(exist_ok=True)

    def generate_txt(
        self,
        unlocked,
        failed,
        already_unlocked
    ):

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        report_path = self.report_folder / f"{timestamp}_Report.txt"

        with open(report_path, "w", encoding="utf-8") as file:

            file.write("=" * 60 + "\n")
            file.write("PDF Unlocker Pro Report\n")
            file.write("=" * 60 + "\n\n")

            file.write(f"Generated : {datetime.now()}\n\n")

            file.write("SUMMARY\n")
            file.write("-" * 60 + "\n")

            total = (
                len(unlocked)
                + len(failed)
                + len(already_unlocked)
            )

            file.write(f"Total PDFs          : {total}\n")
            file.write(f"Unlocked           : {len(unlocked)}\n")
            file.write(f"Already Unlocked   : {len(already_unlocked)}\n")
            file.write(f"Failed             : {len(failed)}\n\n")

            file.write("=" * 60 + "\n")
            file.write("UNLOCKED FILES\n")
            file.write("=" * 60 + "\n")

            for pdf in unlocked:
                file.write(f"{pdf}\n")

            file.write("\n")

            file.write("=" * 60 + "\n")
            file.write("ALREADY UNLOCKED\n")
            file.write("=" * 60 + "\n")

            for pdf in already_unlocked:
                file.write(f"{pdf}\n")

            file.write("\n")

            file.write("=" * 60 + "\n")
            file.write("FAILED FILES\n")
            file.write("=" * 60 + "\n")

            for pdf in failed:
                file.write(f"{pdf}\n")

        return report_path