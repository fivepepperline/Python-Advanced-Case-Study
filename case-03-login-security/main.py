import re

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


if __name__ == "__main__":
    user = User("galang01", "Python123")
    print("Username:", user.username)
    print("User berhasil dibuat.")


# Akun yang terdaftar
akun_terdaftar = User("galang01", "Python123")


# Fungsi login
def login(username, password):
    try:
        user = User(username, password)
    except ValueError as error:
        print(f"Login ditolak: {error}")
        return False

    if user.username != akun_terdaftar.username:
        print("Login ditolak: Username tidak terdaftar.")
        return False

    if user.password != akun_terdaftar.password:
        print("Login ditolak: Password salah.")
        return False

    print("Login berhasil.")
    return True


if __name__ == "__main__":
    print("PENGUJIAN LOGIN")

    login("galang!", "Python123")
    login("galang01", "Ab1")
    login("galang01", "PythonOnly")
    login("galang01", "Python123")