# Python Advanced Topics — Case Studies

Repository ini berisi tiga studi kasus Python yang dibuat untuk menerapkan beberapa konsep lanjutan dalam pemrograman Python. Setiap studi kasus memiliki program, dokumentasi, dan screenshot hasil eksekusi.

## Identitas

* **Nama:** [Nama Lengkap]
* **NIM:** [NIM]
* **Mata Kuliah:** [Nama Mata Kuliah]
* **Program Studi:** Teknik Informatika

## Daftar Studi Kasus

### Case 1 — Analisis Nilai Mahasiswa

Program ini digunakan untuk menghitung nilai akhir mahasiswa berdasarkan nilai tugas, UTS, dan UAS. Program juga menampilkan mahasiswa dengan nilai akhir di atas 80, mengurutkan peringkat mahasiswa, dan menentukan mahasiswa dengan nilai tertinggi.

**Konsep Python yang digunakan:**

* List dan dictionary
* List comprehension
* Filtering data
* `sorted()` dan `lambda`

### Case 2 — IoT Sensor Generator

Program ini mensimulasikan pembacaan suhu dari sensor IoT. Suhu dihasilkan secara bertahap menggunakan generator, kemudian dikelompokkan menjadi kategori Dingin, Normal, atau Panas.

**Konsep Python yang digunakan:**

* Generator dan `yield`
* Modul `random`
* Perulangan
* Kondisi `if`, `elif`, dan `else`
* Pemrosesan data secara bertahap

### Case 3 — Account Security and Audit Log

Program ini menerapkan validasi username dan password serta mencatat setiap percobaan login. Username dan password diperiksa menggunakan regular expression dan aturan validasi, sedangkan aktivitas login dicatat melalui decorator.

**Konsep Python yang digunakan:**

* Class dan object
* Encapsulation menggunakan `@property`
* Regular expression (`re`)
* Decorator
* Timestamp dan audit log

## Struktur Repository

```text
python-advanced-case-study/
├── README.md
├── case-01-analisis-nilai/
│   ├── main.py
│   ├── README.md
│   └── output.png
├── case-02-iot-generator/
│   ├── main.py
│   ├── README.md
│   └── output.png
└── case-03-login-security/
    ├── main.py
    ├── README.md
    └── output.png
```

## Persyaratan

* Python 3
* Terminal atau command prompt
* Editor kode seperti Visual Studio Code

Ketiga program menggunakan modul bawaan Python sehingga tidak memerlukan instalasi library eksternal.

## Cara Menjalankan Program

Buka terminal pada folder repository, lalu jalankan program sesuai studi kasus yang ingin diuji.

**Case 1 — Analisis Nilai Mahasiswa**

```bash
python case-01-analisis-nilai/main.py
```

**Case 2 — IoT Sensor Generator**

```bash
python case-02-iot-generator/main.py
```

**Case 3 — Account Security and Audit Log**

```bash
python case-03-login-security/main.py
```

## Hasil Pengerjaan

Setiap studi kasus dilengkapi dengan file `main.py` untuk menjalankan program, `README.md` untuk menjelaskan program, dan `output.png` untuk menunjukkan hasil eksekusi.

## Status Pengerjaan

*  Case 1 — Analisis Nilai Mahasiswa
*  Case 2 — IoT Sensor Generator
*  Case 3 — Account Security and Audit Log
*  Pemeriksaan akhir seluruh repository
