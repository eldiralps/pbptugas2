##  Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
- Asynchronous programming adalah proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Artinya user dapat mengirim multiple request ke server karena program berjalan secara paralel
- Synchronous programming adalah proses jalannya program secara sequential , disini yang dimaksud sequential ada berdasarkan antrian ekseskusi program. Artinya, user hanya dapat mengirimkan satu request ke server dan dapat mengirimkan request lagi jika request sebelumnya sudah selesai.

## Paradigma Event-Driven Programming.
Pada tugas 6, terdapat salah satu paradigma event-driven programming yaitu saat user klik tombol add task, maka web app akan menampilkan sebuah modal tanpa harus me-reload keseluruhan halaman.

## Jelaskan penerapan asynchronous programming pada AJAX.
AJAX menerapkan asynchronous programming dimana pengunjung web app dapat lebih nyaman mengakses website tanpa perlu berulang kali reload halaman. Hal ini terjadi karena AJAX hanya mengirimkan sebagian data yang dibutuhkan untuk proses saja, tidak keseluruhan sehingga dapat bekerja secara paralel. 


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat path /todolist/json pada urls.py dengan function yang sesuai (yaitu show_data_in_json())untuk mengembalikan seluruh data task dalam bentuk json dan menggunakan AJAX G
- Membuat file todolist_ajax.html, kemudian tambahkan tombol Add Task unutk membuka sebuah modal dengan form
- Membuat path /todolist/add dengan function yang sesuai (yaitu add_task) untuk menambahkan task baru