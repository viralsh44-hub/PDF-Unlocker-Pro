from dataclasses import dataclass


@dataclass
class PDFResult:
    pdf_name: str
    status: str
    password: str = ""
    password_source: str = ""
    error: str = ""
    time_taken: float = 0.0