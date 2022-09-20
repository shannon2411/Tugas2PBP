## Link Heroku

## Perbedaan JSON, XML, dan HTML
1. JSON atau JavaScript Object Notation merupakan suatu format yang dibuat di atas JavaScript untuk merepresentasikan data dalam bentuk key dan value. JSON dapat digunakan untuk melakukan penyimpanan dan pertukaran data dengan cepat dikarenakan strukturnya yang dapat menyimpan data dalam bentuk array, tetapi lebih sulit untuk dibaca oleh manusia daripada XML.
2. XML atau Extensible Markup Language merupakan suatu markup language yang digunakan untuk menyederhanakan proses penyimpanan dan pengiriman data antarserver. XML cenderung menyimpan data dalam format teks sederhana seperti tree yang mirip dengan HTML. Format ini cenderung mudah dibaca oleh manusia dibandingkan format JSON, tetapi pertukaran data akan berlangsung lebih lama.
3. HTML atau HyperText Markup Language merupakan sebuah markup language yang berfokus pada penyajian data. Biasanya data yang direpresentasikan lebih ditujukan untuk Web.

## Alasan diperlukan data delivery dalam pengimplementasian platform
Di dalam suatu platform terkadang ada pertukaran data antara clients dan juga server. Data delivery memudahkan suatu platform untuk melakukan pengiriman data. Data tersebut tentu memerlukan berbagai format dalam pertukarannya. Format yang seringkali digunakan adalah HTML, JSON, dan XML. Dengan adanya format ini, data yang kompleks dapat diatur dalam format tertentu yang dapat dipahami oleh berbagai bahasa pemrograman dan API sehingga dapat mempermudah pengiriman data.

## Langkah-langkah implementasi
1. Menggunakan perintah python manage.py startapp mywatchlist untuk membuat aplikasi di direktori repository yang ingin dibuat.
2. Menambahkan path('mywatchlist/', include('mywatchlist.urls')), di urls.py pada urlpatterns di django_project untuk menghubungkan ke urls.py pada mywatchlist. Lalu pada urls.py di mywatchlist menambahkan urlpatterns = [ ..., path('xml/', show_xml, name='show_xml'), path('json/', show_json, name='show_json'), path('html/', show_watchlist, name='show_watchlist'), ... ] untuk mapping path tertentu terhadap fungsi view yang ingin ditampilkan
3. Membuat model baru pada models.py di mywatchlist bernama MyWatchList dengan fields watched, title, rating, release_date, dan review. Lalu, dilakukan migrasi agar model dibuat pada database.

## Postman
**JSON**
[JSON](https://drive.google.com/file/d/1UlZ1SrXvkWvcuOSPJgAnE94xfKYB6g8D/view?usp=sharing)
**XML**
[XML](https://drive.google.com/file/d/17Xc2-VXA8j_vMABaqAWQaOK5u1tQtgj_/view?usp=sharing)
**HTML**
[HTML](https://drive.google.com/file/d/1Wi1w51jqT5-NKACB1lsWw-E0GQlDl3wf/view?usp=sharing)