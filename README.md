# Tugas Kecil 3 Strategi Algoritma
> Implementasi Algoritma A* untuk Menentukan Lintasan Terpendek

## Shortcuts
* [Deskripsi Program](#deskripsi-program)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Executing The Program](#executing-the-program)
* [Features](#features)
* [Developers](#developers)

## Deskripsi Program
Program ini merupakan program yang dibuat sebagai bentuk pencarian solusi dalam mencari jalur terpendek dari sebuah tempat menuju tempat lain. Permasalahan ini direpresentasikan dalam bentuk graf berbobot yang diterima dalam bentuk file dengan setiap simpulnya adalah tempat-tempat yang ada dan setiap sisinya adalah jarak Harvesine yang telah dihitung. Pencarian jalur terpendek dilakukan dengan menggunakan Algoritma A* dengan input berupa dua buah simpul, yang masing-masing simpul asal dan simpul tujuan. Program akan memberikan keluaran berupa jalur yang dihasilkan dari A* melalui CLI, serta memberikan pilihan visualisasi graf melalui NetworkX dan Matplotlib, atau dengan HERE Maps API melalui media Flask.

## Screenshots
* Contoh Visualisasi Graf Awal dengan NetworkX
![Screenshot (466)](https://user-images.githubusercontent.com/63536655/113722826-fc229200-971a-11eb-9664-e959672f7446.png)
* Contoh Visualisasi Graf Hasil A* dengan NetworkX
![Capture](https://user-images.githubusercontent.com/60037073/113727505-62111880-971f-11eb-93a5-54e8abbc05ad.JPG)
* Contoh Visualisasi Graf Hasil A* dengan NetworkX (2)
![Capture](https://user-images.githubusercontent.com/60037073/113727592-781ed900-971f-11eb-90a7-43dad4b25e7c.JPG)
* Contoh Visualisasi Graf dengan HERE Maps API
![Screenshot (474)](https://user-images.githubusercontent.com/63536655/113724330-70aa0080-971c-11eb-8740-ffe46aed9427.png)
* Contoh Visualisasi Graf dengan HERE Maps API (2)
![Screenshot (473)](https://user-images.githubusercontent.com/63536655/113724352-756eb480-971c-11eb-9be1-6e3e9fb27366.png)


## Technologies
* Flask
* Python
* NetworkX
* Matplotlib
* HERE Maps API

## Setup
Pastikan bahwa semua library digunakan di dalam program sudah terinstall dengan baik. Jika belum ada, gunakan beberapa command PIP untuk melakukan instalasi. Beberapa command tersebut adalah sebagai berikut:
* `pip install networkx`
* `pip install matplotlib`
* `pip install flask`
* Jika masih mengalami kesalahan, lihat dokumentasi setiap instalasi library di [PyPi](https://pypi.org/).
* Untuk Python, unduh *installer* Python 3.x melalui situs resmi berikut, lalu ikuti petunjuk instalasi program. [Python](https://www.python.org/downloads/)

## Executing The Program
* Lakukan pemindahan direktori program melalui Command Prompt atau Terminal dengan command `cd <nama_directory>` ke tempat penyimpanan kode program ini.
* Pastikan file testcase atau file yang ingin dibaca berada dalam satu direktori yang sama jika tidak ingin menginput nama direktori secara lengkap, atau masukkan nama direktori lengkap dengan nama file jika diletakkan pada folder berbeda.
* Eksekusi program dengan menggunakan command `python Tucil3_13519087.py`.
* Ikuti instruksi program yang telah diberikan dalam bentuk Command Line.

## Features
Spesifikasi fitur yang tersedia di dalam program:
* Membaca input file .txt berisi informasi mengenai graf. Informasi mengenai isi file bisa dilihat pada contoh dalam folder `test`.
* Memberikan visualisasi awal bentuk graf yang diterima dari file.
* Pilihan input berupa menjalankan A*, memasukkan file baru, atau keluar dari program.
* Menampilkan output dari pencarian A* dalam bentuk teks dan secara visual melalui NetworkX dan Flask menggunakan HERE Maps API.

Spesifikasi fitur yang bisa dilakukan untuk memperbaiki program:
* Menggunakan Google Maps API dalam visualisasinya

## Developers
* Hizkia R. 13519087
* Richard R. 13519185
