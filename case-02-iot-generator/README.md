# Case 2: Streaming Data Sensor IOT Hemat Memori 

# Deskripsi 
Program ini dibuat untuk membaca data berbasis streaming (aliran bertahap). Komputer hanya memproduksi dan menjalankan data yang diminta, agar tidak semuanya dimuat dalam ram. Sehingga membuat kinerja memori dan server menjadi berat. 

# Konsep Generator 
Genarator adalah fungsi khusus yang digunakan untuk menghasilkan deret nilai secara bertahap, bukan sekaligus. Dalam konteks ini generator sangat bergunan untuk memproses data suhu yang sangat besar. Tanpa membuat komputer kehabisan memori. 
Mengapa menghasilkan yield? 
yield adalah kunci utama yang mengubah fungsi biasa menjadi generator. Yield digunakan karena dua fungsi mendasar. 
1. Mengembalikan Nilai Sementara. Sama seperti return, yield mengirimkan nilai ke baris kode yang memanggilnya. 
2. Membekukan State (Keadaaan) Sementara. Berbeda dengan return yang menghancurkan fungsi setelah selesai, yield hanya menghentikan fungsi sementara. FUngsi tersebut akan mengingat posisi terakhirnya, nilai variabel di dalamnya, dan siap digunakan kembali saat diminta data berikutnya (menggunakan perintah next() atau atau lewat pengulangan for). 

# Proses Pembacaan Suhu
Suhu yang masuk akan langsung dikategorikan. Suhu yang di bawah 20 derajat, maka diartikan suhu dingin. Suhu yang diantara 20 derajat hingga 30 derajat dikategorikan sebagai suhu normal. Suhu yang di atas 30 derajat maka dikategorikan sebagai suhu panas. Seluruh satuan suhu menggunakan satuan Celcius. 

# Ketentuan Program 
* Rentang suhu 15 hingga 38 celcius. 
* Minimal pembacaan 10 kali. 
* Data dihasilkan secara bertahap menggunakan generator. 

# Cara Menjalankan Program
1. Pastikan Python sudah terpasang.
2. Buka terminal di folder `case-01-analisis-nilai`.
3. Jalankan perintah berikut:

```bash
python main.py
```
# Hasil Program
Program akan menampilkan hasil pembacaan suhu berturut-turut sebanyak 10 kali. 

# Konsep Python yang digunakan
* Iteration Pattern
* Generator Function 
* Memory Optimization