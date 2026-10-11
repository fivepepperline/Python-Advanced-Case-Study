# Case 1: Analisis Nilai Mahasiswa

## Deskripsi

Program ini digunakan untuk menghitung nilai akhir mahasiswa berdasarkan nilai tugas, UTS, dan UAS. Setelah nilai akhir didapatkan, program akan menampilkan mahasiswa yang memiliki nilai di atas 80, mengurutkan nilai mahasiswa dari yang tertinggi, dan menentukan mahasiswa dengan nilai akhir terbaik.

## Ketentuan Nilai

Nilai akhir dihitung menggunakan bobot berikut:

* Tugas: 30%
* UTS: 30%
* UAS: 40%

## Fitur Program

1. Menghitung nilai akhir setiap mahasiswa menggunakan *list comprehension*.
2. Menampilkan mahasiswa dengan nilai akhir di atas 80.
3. Mengurutkan mahasiswa berdasarkan nilai akhir dari tertinggi ke terendah menggunakan `sorted()` dan `lambda`.
4. Menampilkan mahasiswa dengan nilai akhir tertinggi beserta nama, NIM, dan nilai yang diperoleh.

## Data Mahasiswa

Program menggunakan data mahasiswa yang disimpan dalam bentuk *list* berisi *dictionary*. Setiap data mencakup nama, NIM, nilai tugas, UTS, dan UAS.

## Cara Menjalankan

1. Pastikan Python sudah terpasang.
2. Buka terminal di folder `case-01-analisis-nilai`.
3. Jalankan perintah berikut:

```bash
python main.py
```

## Hasil Program

Program menampilkan daftar nilai akhir, mahasiswa dengan nilai di atas 80, peringkat mahasiswa berdasarkan nilai akhir, dan mahasiswa terbaik.

Berdasarkan data yang digunakan, **Lopez** mendapatkan nilai akhir tertinggi sebesar **91,50** dengan NIM `24415003`.

## Konsep Python yang Digunakan

* List dan dictionary
* List comprehension
* `sorted()`
* `lambda`
* Filtering data menggunakan kondisi
