import customtkinter as ctk


class PDFUnlockerGUI:

    def __init__(self):

        # Theme
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Main Window
        self.root = ctk.CTk()
        self.root.title("PDF Unlocker Pro")
        self.root.geometry("1000x700")
        self.root.minsize(900, 650)

        # ==========================
        # Header
        # ==========================

        self.header = ctk.CTkFrame(
            self.root,
            height=70,
            corner_radius=0
        )

        self.header.pack(fill="x")

        self.title = ctk.CTkLabel(
            self.header,
            text="PDF Unlocker Pro",
            font=("Segoe UI", 28, "bold")
        )

        self.title.pack(pady=18)

    def run(self):
        self.root.mainloop()