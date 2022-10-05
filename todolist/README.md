# todolist
[Link Tugas 4 & 5](https://shannon-tugas2-pbp.herokuapp.com/todolist/)

# Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?
{% csrf_token %} pada elemen form digunakan untuk memvalidasi key csrf apakah form disubmit atau diakses oleh user_session yang tepat. Jika tidak ada potongan kode tersebut pada elemen form, maka webiste tetap berjalan dengan baik, tetapi nantinya terdapat beberapa link sensitif yang dapat diakses secara umum sehingga dapat membahayakan akun user.

# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.
Kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }}). Cara membuat form secara manual adalah dengan method post dan mengisi {% csrf_token %}. Lalu, membuat table berisi tr yang di dalamnya kita isi input sesuai dengan spesifikasi yang dibutuhkan. Setelah form disubmit, kita dapat mengakses input yang dimasukkan dengan method request.POST.get(name dari setiap komponen form).

# Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Pertama, user menekan submit button pada form. Lalu, semua data yang diinput tadi diakses dengan method request.POST.get(name komponen form). Setelah itu, kita dapat memasukkan data tersebut ke database dengan method Task.objects.create(). Selanjutnya, agar data tersebut ditampilkan pada HTML sesuai dengan user yang menginput form, kita dapat menggunakan method Task.objects.filter(user=request.user) dalam context. Lalu, pada HTML kita lakukan loop pada object dalam context tadi sambil memasukkan data yang sesuai dengan kolom table yang ada.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Menjalankan python manage.py startapp todolist di folder tugas pada cmd.
2. Menambahkan path('todolist/', include('todolist.urls')), di urls.py project django.
3. Membuat class di todolist/models.py yang berisi fields sesuai ketentuan tugas.
4. Membuat fungsi login, logout, register pada todolist/views.py dan membuat restriksi untuk login atau register sebelum membuat atau melihat to do list.
5. Membuat fungsi show_todolist untuk menampilkan data yang diinput oleh user dengan Task.objects.filter(user=request.user) dan show_create_todo untuk untuk menerima input data dari user dan memasukkannya ke database dengan Task.objects.create()
6. Membuat path dan menyambungkannya dengan fungsi-fungsi di atas dimana fungsi-fungsi tersebut return HTML yang sesuai.
7. Melakukan deploy ke heroku dan membuat 2 user dengan masing-masing 3 dummy list to do.

# Inline vs External vs Internal CSS
Inline adalah ketika meletakkan CSS property pada attribute atau props html tag. External CSS adalah meletakkan CSS atribute di luar dari file html. Caranya dengan membuat file baru dengan extension .css dan melakukan import pada html yang ingin diaplikasikan style dari file css tersebut. Internal CSS adalah di dalam html dengan memanfaatkan style tag. Isi dari tag tersebut sama caranya dengan mengisi css property pada file external.

# HTML Tags
div tag adalah suatu tag yang merepresentasikan sebuah section atau block. Tag title merupakan tag yang berhubungan title yang ada di tab browser. Selain itu, ada tag untuk menerima input dari user, bisa berupa text field atau button submit, checkbox, dll.

# CSS Selector
CSS selector yang saya ketahui ada .class, dengan awal dot(.) berarti merujuk pada value dari property class. #id merujuk pada penggunaan property id pada html tag. * untuk apply ke semua element. kemudian selector juga bisa terdiri dari banyak selector misalnya .class1 .class2. Kemudian juga selector html tag misalnya p, berarti merujuk untuk semua p tag, dll.

# Impelementation Assignment 5
Saya menggunakan bootstrap untuk styling dan mengubah tabel to do list mnejadi cards. Pertama adalah dengan memasukkan link-link untuk mengakses bootstrap di base.html. Bootstrap secara otomatis responsive. Saya mengganti font dan warna untuk text dan button. Saya juga menambahkan background dan memposisikan komponen agar ke tengah dengan mengatur text-align, margin, display, dan width. Untuk bagian cards, untuk responsive cardsnya, saya menambahkan col-lg, col-md, col-sm pada class card.