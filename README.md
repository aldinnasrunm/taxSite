# Tugas mata kuliah Algoritma dan Pemrograman, Kelas X 2022 oleh kelompok WahDeadline
 
Project ini adalah bagian dari tugas besar mata kuliah Algoritma dan Pemrograman, Teknik Informatika, Universitas Muhammadiyah Surakarta, tahun 2022.
 
Dosen : Fajar Suryawan, Ph.D
 
## Bagaimanakah struktur kode aplikasi ini?
Struktur kode
Pertama-tama kita membuat project django baru bernama taxSite, lalu kami buat repo baru juga di github serta mempublish project kami kedalam github tersebut.  
Selanjutnya kami membuat class di apps.py yang akan dipanggil di settings.py. Kemudian membuat beberapa fungsi yang berkaitan dengan aplikasi di myutils.py untuk diimport ke views.py.
Untuk berpindah dari index ke about atau sebaliknya, kita buat definisi untuk masing-masing page dan kita masukan return render agar page dapat ter load tak lupa menambahkan lokasi dari file nya (misal: tax/index.html)di views.py. Setelah membuat definisi untuk setiap page, kita buat path di urls.py dengan menambahkan nama path yang yang sama dengan nama definisi kita di views.py tadi.
Untuk mengimport gambar, kita bisa gunakan layanan github untuk mengupload gambar kita lalu kita copas alamat raw gambar ke code kita, karena kita tidak bisa menggunakan gambar yang tersimpan di local (offline). Kita juga bisa menggunakan google font dan menggunakan css di dalam file html tepatnya di tags style
Untuk settings.py time zone diubah menjadi Asia/Jakarta supaya jam nya bisa mengikuti sesuai dengan zona waktu WIB .
 Mind map:
    membuat class di apps.py → menambah class tadi ke installed app di settings.py → membuat fungsi yang diperlukan di myutils.py → membuat definisi untuk masing-masing page serta mengimport fungsi dari myutils.py ke views.py → membuat path link dan memanggil definisi page kita di views.py tadi ke urls.py → membuat folder templates → mulai mengedit index dan about .
Setelah semua itu selesai lalu membuat file readme untuk informasi lalu merge semua file yang berada di branch saat ini ke branch master . Setelah itu deploy aplikasi ke heroku dengan cara membuat procfile terlebih dahulu lalu push lewat git push heroku master.
 
Definisi dan fungsi setiap file :
Taxite		: Berisi app yang akan digunakan dalam menyimpan serta mengelompokkan kode-kode yang dibutuhkan. Didalamnya terdapat folder:
Config 		: Berisikan file pengaturan Django berisi semua konfigurasi instalasi Django. File-file di folder ini menjelaskan cara kerja pengaturan dan pengaturan mana yang tersedia.
Tax		    : Berisikan file yang digunakan untuk menyimpan kode untuk menghitung pajak. Didalamnya terdapat folder:
Template tax	: Tempat menyimpan file yang berisikan kode untuk ditampilkan dalam web. Didalamnya terdapat 2 file:
Index.html : untuk menyimpan kode yang digunakan  untuk menghitung pajak progresif diantaranya seperti form input, table, kelompok, dosen pengampu, serta waktu.
about.html : untuk menampilkan halaman yang berisikan about page, pengertian dari pajak progresif, dan ilustrasi diagram serta kontribusi dari anggota kelompok.
Urls	    : untuk menyimpan kode yang akan berkaitan dengan link yang akan digunakan untuk berpindah halaman dan merefresh halaman.
Settings	: File inti dalam proyek Django. Ini menampung semua nilai konfigurasi yang dibutuhkan aplikasi web untuk bekerja.
Myutils   	: Untuk menyimpan kode definisi yang digunakan untuk menghitung pajak.
Views 		: Untuk menyimpan kode fungsi terusan dari myutils .Dan untuk diteruskan ke index, about dan urls . Didalam views juga ada fungsi exception dan error handling .
Procfile  	: digunakan untuk deploy ke Heroku. 

## Akses Aplikasi di Heroku: 
https://tax-2021-agus-aldin-nabila.herokuapp.com/
 
## Anggota Kelompok:
1. Agus Ardiansyah Nh, L200214197
2. Aldin Nasrun Minalloh, L200214208
3. Hanifah Afkar Nabila, L200214252
 
## Daftar kontribusi :
1. Agus  	: Membuat style and logic untuk about.html, menjelaskan project di readme.md, deploy app ke heroku
2. Aldin	: Membuat style and logic untuk index.html, add logic into myutils, setting urls.py
3. Nabila	: Membuat logic untuk views, melengkapi dan mengedit readme.md, full design about page di figma
