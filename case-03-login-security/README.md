# Case 3: Account Security and Audit Log 

## Deskripsi Program
Program ini menjalakan proses login. Proses login harus ada verifikasi dan aturan format kredensial agar akun terlindung. Juga menyimpan aktivitas login baik berhasil maupun gagal tanpa mengotori alur kode utama. 

## Validasi Data Pengguna
Berikut adalah ketentuan validasi,
* Username: minimal 5 karakter, hanya boleh berupa kombinasi huruf dan angka(alfanumerik), tanpa spasi dan simbol aneh. 
* Password: minimal 8 karakter dan wajib memuat setidaknya satu karakter angka. 
* Pemeriksaan format username dan passwor dwajib menggunakan ekspresi reguler`(RegEx)`. 

## Konsep Encapsulation 
1. *class* User adalah sebuah wadah yang menyimpan objek user dan password. 
2. `@properti` adalah sebuah dekorator (fitur khusus Python) yang digunakan untuk mengubah sebuah fungsi (method) di dalam kelas agar bisa diakses seolah-olah ia adalah variable/atribut biasa. 

Keduanya dikombinasikan untuk memperkuat keamanan dan validasi data. 
`@properti` bekerja di dalam *class* User melalui 3 peran. 
    1. Getter (Mengambil Data), digunakan saat mengambil data pengguna atau menyajikan data yang sudah diformat. 
    2. Setter (Mengubah & Memvalidasi Data), digunakan untuk memeriksa kondisinya sesuai standar atau tidak. 
    3. Read-Only Property, ada kalanya data pengguna tidak boleh diubah sama sekali dari luar, misalnya user_id atau tanggal akun dibuat. Dengan @property tanpa membuat @setter, data tersebut otomatis terkunci dan aman dari perubahan tidak sengaja.

## Validasi Mengguanakan RegEx
`RegEx` *(Regular Expression)* adalah pola pencocokkan teks otomatis untuk menyaring data pengguna. 

## Audit Log
Informasi yang dicatat sistem saat aktivitas login adalah sebagai berikut: 
* Login berhasil: mencatat tanggal dan jam kejadian (timestap), nama pengguna (username), serta status akses "Succes". Digunakan sebagai bukti sah bahwa pengguna berhasil masuk ke dalam sistem. 
* Login ditolak: mencatat tanggal dan jam kejadian, nama pengguna yang dicoba, serta status "failed" berserta alasan penolakan (misalnya: wrong password atau invalid username format berdasarkan RegEx). Berfungsi mendeteksi indikasi serangan brute-force atau pencobaan akses illegal. 

## Cara Menjalankan Program 
1. Pastikan Python sudah terpasang.
2. Buka terminal di folder `case-03-login-security`.
3. Jalankan perintah berikut:

```bash
python main.py
```
## Skenario Pengujian 
Username tidak valid.
Password kurang dari 8 karakter.
Password tidak mengandung angka.
Login berhasil menggunakan data yang valid.

## Konsep Python yang Digunakan
Class dan object
Encapsulation dengan @property
Regular expression (re)
Decorator atau closure
Timestamp untuk pencatatan aktivitas