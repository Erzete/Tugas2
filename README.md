# Jawaban Tugas

## Tugas 2
Link : https://tugas2-rt.herokuapp.com/katalog/

1. https://ibb.co/X5SmKD6
2. Kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment tetapi tentunya akan lebih baik menggunakan Virtual environment
   Hal ini dikarenakan kita membutuhkan semacam sekat/batasan untuk setiap proyek Django, sehingga satu proyek dengan proyek lainnya tidak akan terganggu. Hal
   ini juga akan mencegah error ketika misalnya ada proyek yang menggunakan versi/dependencies yang berbeda.
3. Bagaimana cara saya melakukan tahap 1-4? Simpelnya ya tentu saja dengan tinggal mengikuti tutorial 2 yang telah ada. Kemudian saya ubah beberapa method, variabel
   yang ada untuk menyesuaikan dengan proyek katalog dan bukan wishlist (seperti nama method show_wishlist menjadi show_katalog dan menambahkan npm pada views. 
   Kemudian tentunya karena datanya berbeda saya juga harus menambahkan beberapa hal pada models.py Mungkin seperti itu saja sama dengan lainnya seperti .html
   Ketika deployment-nya saya mengalami  beberapa isu karena ketidakmen gertian saya terhadap Heroku. Akan tetapi, akhirnya saya bisa menemukan yang mana yang salah 
   sehingga saya bisa men-deploy project django ini ke Heroku.
   
## Tugas 3
Link : https://tugas3-rt.herokuapp.com/mywatchlist/html/, https://tugas3-rt.herokuapp.com/mywatchlist/xml/, https://tugas3-rt.herokuapp.com/mywatchlist/json/

Postman : https://imgur.com/a/FLAKjR0

1. JSON = Buat merepresentasikan objek, tidak ada end tag, ga bisa komen di file-nya, cuma bisa pake UTF-8 encoding
   XML = Dynamic, Markup language, menyimpan dan membawa data, ada start dan end tag, bisa komen, bisa pake encoding selain UTF-8, nama tags-nya bisa ditentukan                sendiri oleh user
   HTML = Static, fokusnya lebih ke tata (representasi) objek, teks, dan data pada web, bisa komen, bisa pake encoding lain dari UTF-8, tags 
          dalam HTML udah ada dari sananya., ada end tag tapi ga harus
2. Data delivery penting karena data ada bermacam-macam bentuknya baik dalam .json, .xml, .html, dan lain sebagainya. Pada kalanya data yang ada pada suatu file data      kita ingin untuk load atau direpresentasikan pada file data lainnya, ini salah satu pentingnya data delivery. Selain itu, dengan data delivery jika suatu data          membutuhkan data yang lain maka data itu akan tersedia.
3. Awal saya buat dulu app nya memakai 
   > python manage.py startapp mywatchlist
   
   Kemudian saya melakukannya seperti hal yang ada pada Lab 1 dan 2 bedanya di folder mywatchlist models.py saya isi dengan atribut yang ada pada soal. Kemudian saya      juga membuat initial_mywatchlist_data.json yang isinya 10 film beserta atributnya sesuai dengan yang ada pada models.py jangan lupa sama seperti lab 2 kita akan        menampilkan xml dan json-nya. Kemudian pada test.py saya mencoba untuk mengakses ketiga function yang ada pada views.py, semuanya udah OK. 
  
## Tugas 4

1. Kegunaan dari csrf_token sesuai namanya adalah sebagai proteksi website terhadapt Cross Site Request Forgeries. Jika pada laman terdapat kelemahan seperti yang        telah disebutkan maka suatu user bisa saja menjalankan hal yang mereka sebenarnya tidak inginkan terjadi seperti menghapus akun user ataupun hanya sekedar me-logout    user dari akunnya.
2. Ya tentu saja bisa, kita tinggal membuatnya dengan <form></form> isi body form tersebut terdiri dari label (untuk menunjukkan apa yang perlu diisikan user) dan        input beserta tipe input yang kita inginkan dari user.
3. Setelah kita mengisi form yang terdapat pada html, isian tersebut akan disimpan oleh database yang berisi objek-objek yang dimiliki oleh Task. Nah, ketika kita        ingin memunculkannya kita tinggal me-request data tersebut menggunakan show_todolist, objek Task akan difilter sesuai dengan user yang sedang logged in kemudian        akan dimunculkan dengan render
4. Untuk register, login, logout kurang lebih sama dengan yang ada di tutorial3, namun untuk show_todolist kita tidak akan memunculkan semua objek Task melainkan          difilter berdasarkan user yang sedang login. Kemudian saya tambahkan function add_task pada views yang berguna untuk menambah objek Task, function ini akan            bekerjasama form.html dan juga forms.py untuk menyimpan data tersebut. Jangan lupa tambahkan button tambah task baru yang akan meng-redirect user ke halaman yang      berisi form.html

Mungkin itu saja, terima kasih telah membaca README ini
Salam,
Rama Tridigdaya
