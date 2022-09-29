[LINK APLIKASI](http://mvt-djangoapp.herokuapp.com/todolist/login) <br>
<br>
<hr>
Jawaban dari Pertanyaan: <br>
<br>

1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>? <br>
{% csrf_token %} merupakan salah satu emplate tag yang menyediakan perlindungan yang mudah digunakan terhadap Cross Site Forgery Request. Jenis serangan ini terjadi ketika situs web berbahaya berisi tautan, tombol formulir, atau beberapa JavaScript yang dimaksudkan untuk melakukan beberapa tindakan di situs web yang kita miliki, menggunakan kredensial pengguna yang masuk yang mengunjungi situs jahat di browser mereka. Jenis serangan terkait, 'login CSRF', di mana situs penyerang menipu browser pengguna untuk masuk ke situs dengan kredensial orang lain juga. Dengan {% csrf_token %}, templat akan merender elemen tersembunyi dengan nilai yang disetel ke token CSRF. Ketika server Django menerima permintaan formulir, Django akan memverifikasi bahwa token cocok dengan nilai yang diberikan dalam formulir. Ini diperlukan untuk memastikan bahwa POST permintaan (misalnya permintaan pengubah data) berasal dari sesi klien yang authentic.<br>
Apabila kita tidak menambahkan potongan kode {% csrf_token %} pada elemen form, maka akan menampilkan error berupa CSRF token mismatch.
<br>

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa mengggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual. <br>
Ya, dengan cara merender setiap field secara manual, seperti pada potongan kode berikut ini.<br>
[CONTOH KODE](https://drive.google.com/file/d/1yoZo4Pc_o-tHQD_9exNI4fxMYUODtOpk/view?usp=sharing)
<br>

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML. <br>
1) User akan mengirimkan request berupa address kepada browser yang kemudian browser akan generate HTTP request yang akan diterima oleh server.<br>
2) Server akan memilah-milah fungsi di views.py yang sesuai untuk menghandle path yang diterima sebelumnya, kemudian server men-generate HTML page FORM berdasarkan behavior method yang dipanggil pada views.py.<br>
3) Selanjutnya, browser akan menampilkan layout kepada user sehingga user dapat mengisi input-input yang diperlukan dapat form tersebut.<br>
4) Setelah user menginputkan data-data yang diperlukan, broser menghasilkan HTTP request, method, dan argument meuju URL Destination berdasarkan HTML page Form. <br>
5) Server menerima HTTP request, kemudian memilih-milih fungsi pada views.py yang sesuai dan melakukan behavior sesuai fungsi sebelumnya (memasukan inputan user ke dalam database dengan fungsi yang bersesuaian) kemudian men-generate kembali HTML page. <br>
6) Tahap terakhir adalah browser menampilkan kembali HTML layout kepada user. <br>
<br>

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.<br>
1) Membuat Aplikasi Django beserta Konfigurasi Model
- Mengaktifkan virtual environment.
- Membuat app todolist dengan perintah python manage.py startapp todolist
- Menambahkan aplikasi todolist ke dalam variabel ISTALLED_APPS pada file settings.py project_django
- Membuka models.py dan menambahkan class Task dengan atrribute berupa user, date, title, dan description
- Melakukan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal.
- Menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal. <br>

2) Implementasi form registrasi, login, dan logout
- Membuka views.py, import redirect, UserCreationForm, dan messages
- Membuat fungsi register() untuk menghasilkan form registrasi secara otomatis.
- Membuat file register.html pada folder todolist/templates untuk menampilkan HTML page Form
- Membuat urls.py pada folder todolist untuk melakukan routing terhadap fungsi register yang telah dibuat sebelumnya.
- Membuka views.py, kemudian import authenticate & login.
- Membuat fungsi login_user() untuk mengautentikasi pengguna yang ingin login.
- Membuat berkas HTML yaitu login.html pada folder todolist/templates
- Membuka urls.py kemudian import login_user serta tambahkan path ke varabel urlpatterns.
- Membuka views.py, kemudian import logout pada vies.py dan tambahkan fungsi logout_user().
- Membuka urls.py dan import fungsi logout_user, dan menambahkan path pada urlpatterns.<br>
3) Membuat Halaman Utama Todolist
- Membuat fungsi show_todolist pada views.py
- Menambahkan path todolist pada file urls.py di folder project_django dan menambahkan path pada variabel urlpatterns di urls.py pada folder todolist.
- Membuat file html yakni todolist.html, membuat tabel yang isinya berupa iterasi dari setiap task yang baru ditambahkan, tombol Tambah Task Baru, dan tombol Logout. <br>
4) Membuat Task Form
- Membuat class TaskForm pada forms.py sebagai blueprint dari Form yang akan digunakan
- Membuat fungsi create_task pada views.py yang akan mengimplementasikan behavior penambahakn task berdasarkan username yang sesuai.
- Menambahkan routing dengan cara menambahkan path pada variabel urlpatterns pada urls-py terhadap fungsi create_task yang telah dibuat
- Membuat html file create-task.html untuk menampilkan TaskForm yang sudah dibuat berdasarkan views.py
- buka admin.py, kemudian tambahkan code admin.site.register(Task) dan jalankan perintah python manage.py createsuperuser <br>

5) Mendeploy ke Heroku
- Lakukan git add, commit, dan push kemudian jalankan aplikasinya yang telah di-deploy ke Heroku dan mendaftarkan 2 akun pengguna dan tiga dummy data.


