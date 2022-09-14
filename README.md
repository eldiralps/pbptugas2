[LINK APLIKASI](https://dashboard.heroku.com/apps/mvt-djangoapp) <br>
[BAGAN](https://drive.google.com/file/d/1x0t_L8MGvQT8vm0xjlLMYXXwQCyWYQy1/view?usp=sharing) <br>
<br>
<hr>
Jawaban dari Pertanyaan: <br>
<br>
1.Pada bagan tersebut, pertama-tama user akan mengirimkan HTTP request ke dalam server Django yang kemudian akan diproses melalui URLS (urls.py). File urls.py akan melakukan routing terhadap fungsi-fungsi yang ada pada View terhadap request yang dikirim oleh user sebelumnya. View berperan sebagai logika utama dari aplikasi yang akan melakukan pemrosesan terhadap permintaan yang masuk. Isi dari file views.py merupakan fungsi-fungsi yang dapat digunakan untuk memproses permintaan client. Untuk melakukan pemrosesan terhadap permintaan client, tak jarang di dalam prosesnya memerlukan keterlibatan database. Oleh karena database tidak dapat diakses secara langsung karena bersifat rahasia dan rawan terjadi modifikasi jika dapat diakses secara langsung melalui server, maka terdapat suatu arsitektur bernama Model yang akan melakukan traksaksi data dengan database. Dari sinilah kemudian terjadi tahapan di mana View akan memanggil query ke Model yang kemudian disalurkan pada database (terjadi transaksi data) dan Model  akan mengembalikan hasil dari query tersebut kembali ke View. Setelah permintaan client tersebut selesai diproses oleh View, hasil proses tersebut kemudian  akan dipetakan ke dalam Template file HTML yang sudah di definisikan sebelumnya. Terakhir, file HTML tersebut dikembalikan kepada pengguna sebagai respons dari permintaan client berupa tampilan halaman web-nya.<br>
<br>
2.Dalam membuat web app berbasis Django, kita disarankan untuk membuat virtual environment. Virtual environment berguna untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada computer yang kita miliki. Jadi, apabila kita ingin menjalankan aplikasi yang telah kita buat melalui device lain (yang berbeda dengan yang kita gunakan saat membangun aplikasi), dimana device tersebut memiliki versi yang berbeda (asumsikan aplikasi yang kita buat menggunakan python versi 3.9, sementara device baru yang ingin kita gunakan masih memakai python versi 3.4 sehingga terdapat package ataupun dependencies yang tidak dapat digunakan di aplikasi yang telah kita buat saat kita menggunakan device yang berbeda dengan device yang kita gunakan saat membuat aplikasi), sehingga aplikasi yang telah kita buat tidak akan bekerja dengan semestinya. Oleh karena itu, agar aplikasi yang telah kita buat sebelumnya tetap bekerja dengan baik meskipun memiliki versi yang berbeda, maka kita disarankan untuk menggunakan virtual environment. Namun demikian, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, tetapi disarankan pada setiap aplikasi yang kita buat menggunakan virtual environment agar aplikasi yang kita buat dapat berjalan secara optimal.<br>
<br>
3a.Akan dibuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML yakni fungsi show_catalog() yang menerima parameter request. Body dari funsi show_catalog() berisi pemanggilan fungsi query ke model database dan menyimpan hasil query tersebut ke dalam variabel daftar_katalog. Terakhir, fungsi show_catalog akan mengembalikan render(request, "katalog.html", context). Fungsi render() mengambil permintaan objek sebagai argumen pertamanya (request), nama cetakan sebagai argumen keduanya (“katalog.html”) dan kamus sebagai pilihan argumen ketiganya (context). <br>
<br>
3b.Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
Sebuah routing yang saya lakukan untuk memetakan fungsi show_catalog() pada views.py agar nantinya dapat ditampilkan melalui browser adalah dengan cara menambahkan potongan code pada file urls.py pada direktori katalog. <br>
<br>
from django.urls import path
from katalog.views import show_catalog <br>

app_name = 'katalog' <br>

urlpatterns = [
    path('', show_catalog, name='show_catalog'),
] <br>
<br>
Selain itu, perlu dilakukan pula penambahan potongan code sebagai berikut di dalam variabel urlpatterns pada file project_django.
path('katalog/', include('katalog.urls')),
path digunakan untuk merutekan URL ke fungsi tampilan yang sesuai dalam aplikasi Django menggunakan operator URL. <br>
<br>
3c.Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
Akan dilakukan looping untuk memetakan data-data yang dibutuhkan dengan potongan kode sebagai berikut. <br>
<br>
{% for barang in list_barang %} <br>
      <tr> <br>
        <th>{{barang.item_name}}</th> <br>
        <th>{{barang.item_price}}</th> <br>
        <th>{{barang.item_stock}}</th> <br>
        <th>{{barang.rating}}</th> <br>
        <th>{{barang.description}}</th> <br>
        <th>{{barang.item_url}}</th> <br>
      </tr> <br>
 {% endfor %} <br>
 <br>
Untuk setiap barang yang ada di dalam kamus list_barang, akan dilakukan pemanggilan attribute dari setiap barang yang disimpan dalam variabel item_name, item_price, item_stock, rating, description, dan item_url. <br>
<br>
3d.Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Sebagai persiapann melakukan deployment ke Herokuapp, pertama-tama kita akan melakukan git init pada direktori dari tempat penyimpanan app yang ingin kita deploy. Kemudian, membuat file Bernama Procfile untuk membaca aktivitas log aplikasi ke system monitoring internal Heroku. Setelah itu, dibuat file dpl.yml untuk mengeksekusi deployment oleh runner dari GitHub Actions dan buat juga berkas .gitignore untuk memberi tahu git mengenai berkas atau direktori mana sajakah yang tidak boleh ikut di-push ke repositori. Setelah iu, dilakukan beberapa konfigurasi pada file settings.py proyek Django yang telah kita buat. Terakhir lakukan git add, git commit, dan git push terhadap semua perubahan yang telah dilakukan. <br>
<br>
Tahapan selanjutnya adalah untuk mendeploy ke Heroku.
Pertama-tama kita harus menyalin API Key dari akun Heroku yang kita miliki. Kemudian, kita akan menambahkan variabel repository secret pada bagian Secrets di GitHub dari project yang kita buat. Variabel repository secret berisi pasangan nama value dari variabel yang telah kita miliki sebelumnya yakni: <br>
HEROKU_API_KEY: <VALUE_API_KEY_ANDA> <br>
HEROKU_APP_NAME: <NAMA_APLIKASI_HEROKU_ANDA> <br>
Variabel-variabel tersebut kemudian kita simpan dan refresh kembali laman GitHub, jika terdapat centang hijau pada repository yang kita miliki, maka tandanya deployment yang kita lakukan berhasil. <br>
