
import re
from datetime import datetime

audit_logs = []


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not re.fullmatch(r"[A-Za-z0-9]{5,}", value):
            raise ValueError(
                "Username minimal 5 karakter dan hanya boleh berisi huruf atau angka."
            )
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("Password minimal 8 karakter.")
        if not re.search(r"\d", value):
            raise ValueError("Password harus mengandung minimal 1 angka.")
        self._password = value


def audit_log(func):
    def wrapper(username, password):
        berhasil, alasan = func(username, password)

        status = "BERHASIL" if berhasil else "DITOLAK"

        catatan = {
            "Waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Username": username,
            "Status": status,
            "Alasan": alasan
        }

        audit_logs.append(catatan)
        print(f"Login {status}: {username} - {alasan}")

        return berhasil

    return wrapper


akun_terdaftar = User("galang01", "Python123")


@audit_log
def login(username, password):
    try:
        user = User(username, password)
    except ValueError as error:
        return False, str(error)

    if user.username != akun_terdaftar.username:
        return False, "Username tidak terdaftar."

    if user.password != akun_terdaftar.password:
        return False, "Password salah."

    return True, "Login berhasil."


if __name__ == "__main__":
    print(" PENGUJIAN LOGIN ")

    login("galang!", "Python123")
    login("galang01", "Ab1")
    login("galang01", "PythonOnly")
    login("galang01", "Python123")

    print("\n AUDIT LOG ")

    for log in audit_logs:
        print(
            f"[{log['Waktu']}] "
            f"Username: {log['Username']} | "
            f"Status: {log['Status']} | "
            f"Alasan: {log['Alasan']}"
        )