## Link Heroku
Buka link berikut, [https://shannon-tugas2-pbp.herokuapp.com/katalog/](https://shannon-tugas2-pbp.herokuapp.com/katalog/).

## Bagan
Buka link berikut, [Bagan](https://drive.google.com/file/d/1DDnV3Vw7Qd5DZ9oqEqEqfj3Nnoaw05Vk/view?usp=sharing).

## Virtual Environment
virtual environment berfungsi untuk memisahkan pengaturan dan package yang diinstall pada setiap proyek Django sehingga perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment.

## Implementasi
**Persiapan**
1. Clone repository, membuat & menyalakan virtual environment, install dependencies
2. Mempersiapkan migrasi skema model ke dalam database Django lokal, menerapkan skema model yang telah dibuat ke dalam database Django lokal, dan memasukkan data tersebut ke dalam database Django lokal.

**Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML**
1. Membuka views.py yang ada pada folder katalog dan membuat sebuah fungsi yang menerima parameter request dan mengembalikan render(request, "katalog.html").
2. Di dalam folder aplikasi katalog, isi urls.py untuk melakukan routing terhadap fungsi views sehingga nantinya halaman HTML dapat ditampilkan lewat browser.
3. Mendaftarkan aplikasi katalog ke dalam urls.py yang ada pada folder project_django.

**Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py**
1. Pada fungsi views yang telah dibuat, import models ke dalam file views.py di folder katalog.
2. Menambahkan kode ke dalam fungsi show_katalog untuk memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel. Menambahkan context sebagai parameter ketiga pada pengembalian fungsi render.

**Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template**
1. Mengubah Fill me! yang ada di dalam HTML tag <p> menjadi {{nama}} dan {{npm}} untuk menampilkan nama dan npm di halaman HTML. Untuk menampilkan daftar barang ke dalam tabel, melakukan iterasi terhadap variabel list_barang yang telah kamu ikut render ke dalam HTML.

**Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet**
1. Membuat aplikasi baru di Heroku dan connnect ke repositori tugas 2.
2. Menambahkan secrets di GitHub untuk HEROKU_API_KEY dan HEROKU_APP_NAME.
3. Membuka GitHub actions dan menjalankan kembali workflow yang gagal.
