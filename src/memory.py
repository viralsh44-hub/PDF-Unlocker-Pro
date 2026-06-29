import json
import os


class PasswordMemory:

    def __init__(self, file_path="config/password_memory.json"):
        self.file_path = file_path
        self.max_passwords = 50
        self._create_file_if_missing()

    def _create_file_if_missing(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump({"recent_passwords": []}, file, indent=4)

    def load_passwords(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            return data.get("recent_passwords", [])

        except Exception:
            return []

    def save_password(self, password):

        if not password:
            return

        passwords = self.load_passwords()

        passwords = [p for p in passwords if p != password]

        passwords.insert(0, password)

        passwords = passwords[:self.max_passwords]

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(
                {"recent_passwords": passwords},
                file,
                indent=4
            )

    def clear_history(self):

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump({"recent_passwords": []}, file, indent=4)

    def get_recent_passwords(self):
        return self.load_passwords()