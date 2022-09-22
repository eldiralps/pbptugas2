[LINK APLIKASI](http://mvt-djangoapp.herokuapp.com/mywatchlist/) <br>
[Screenshot POSTMAN 1](https://drive.google.com/file/d/1-hvWSeRhYxg54zl_UGNE7WupSOxx9qt2/view?usp=sharing) <br>
[Screenshot POSTMAN 2](https://drive.google.com/file/d/11hz08V-ZO81CIUhrSynzhog_E8K2sEdE/view?usp=sharing) <br>
[Screenshot POSTMAN 3](https://drive.google.com/file/d/1VP6T1mwu3VFsJVlOWpt5LgU_vXgvtcTJ/view?usp=sharing) <br>
<br>
1. Jelaskan perbedaan antara JSON, XML, dan HTML! <br>
HTML (HyperText Markup Language) adalah suatu bahasa yang menggunakan tanda-tanda tertentu (tag) untuk menyatakan kode-kode yang harus ditafsirkan oleh browser untuk mengatur dan memformat halaman sebuah website dan dokumen lainnya yang ada di World Wide Web. HTML menitikberatkan pada penyajian data (seperti bagaimana format tampilan suatu data), sementara XML berfokus pada transfer data (berupa struktur dan konteksnya.
Kemudian, perbedaan keduanya dengan JSON hanyalah format data sedangkan HTML dan XML adalah bahasa markup. XML digunakan untuk menyimpan dan mengangkut data dari satu aplikasi ke aplikasi lain melalui Internet. JSON di sisi lain adalah format pertukaran data ringan yang jauh lebih mudah bagi komputer untuk mengurai data yang sedang dikirim.
<br>
Format JSON menggambarkan diri sendiri dan secara komparatif jauh lebih mudah dibaca daripada dokumen berformat XML karena JSON menyimpan semua datanya dalam format map (key / value) . Akan tetapi, jika sebuah proyek memerlukan markup dokumen dan informasi metadata, maka lebih disarankan untuk menggunakan XML.
<br>
2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? <br>
Secara umum, platform seperti website atau aplikasi tersusun atas bagian front end (tampilan untuk user) dan back end (logika aplikasi termasuk data). Frontend dan backend tidak dapat berinteraksi secara langsung untuk pertukaran data, diantara keduanya dibutuhkan perantara untuk menampilkan responses dari request yang diminta oleh user. Untuk menghubungkan front end dengan back end, maka diperlukan adanya data delivery seperti xml dan json. Data delivery akan membantu platform dalam pengolahan data diantara frontend dan backend dan juga mempermudah penyajian informasi dan seluruh komponen dari website sesuai formatting yang diminta oleh user, misal browser request HTML page, maka server juga harus mengembalikan HTML page, berlaku untuk XML, JSON, dan sebagainya.
<br>
3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. <br>
- Mengaktifkan virtual environment <br>
- Membuat aplikasi baru bernama wishlist dengan perintah python manage.py startapp mywatchlist<br>
- Menambahkan aplikasi "mywatchlist" pada variabel INSTALLED_APPS di settings.py folder django-project untuk mendaftarkan aplikasi mywatchlist agar dapat di baca oleh django. <br>
- Membuat model watchlist di direktori mywatchlist dengan atributtes berupa watched, title, rating, release_date, dan review di dalam file models.py.<br>
- Melakukan migrasi data dari models kita agar attribute model kita tersimpan di django database.<br>
- Membuat folder fixtures di folder mywatchlist. Di dalam folder fixtures, kita buat file bernama initial_mywatchlist_data.json.<br>
- Membuat fungsi pada file views.py agar dapat menampilkan data dalam bentuk HTML, XML, dan JSON.<br>
- Membuat routing pada urls.py sehingga fungsi-fungsi yang telah dibuat pada view.py dapat ditampilkan pada web server dengan cara menambahkan path baru sesuai dengan fungsi yang telah dibuat pada file views.py. <br>
- Mendaftarkan aplikasi mywatchlist pada urls.py di dalam folder project_django. <br>
- Melakukan git add, git commit, dan push. <br>
