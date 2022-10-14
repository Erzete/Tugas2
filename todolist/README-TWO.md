# Tugas 6 (Late)
1. Asinkronus : Pengguna tidak harus me-refresh laman untuk mendapatkan data terbarunya, masih bisa berinteraksi dengan web tersebut selama data di-load
   Sinkronus : Untuk mendapatkan data terbaru, laman harus di-refresh oleh user.
2. Event-driven-programming adalah paradigma programming yang berfokus pada event dan alur jalan programnya ditentukan oleh event yang dibuat oleh user. User didorong    untuk berinteraksi dengan web/aplikasi tersebut untuk membuat event2 tersebut. Contohnya pada tugas ini adalah Tombol "Submit Task" yang akan menjalankan              addTodolist
   ketika ditekan.
3. AJAX akan membuat halaman web memperbarui datanya secara asinkronus dengan mengirimkan data ke server di balik layar, AJAX menggunakan browser untuk meminta data      dari web server dan JavaScript, menggunakan XML/JSON untuk mengirim data, serta HTML DOM untuk menampilkan data. 
4. Untuk GET, saya menggunakan getJSON untuk mengambil json yang ada di todolist/show_json, kemudian saya akan me-loop setiap data yang ada pada json tersebut untuk
   membuat Card yang sesuai dengan format pada tugas sebelumnya dan nanti hasilnya akan ditampilkan pada laman. Untuk POST, saya membuat fungsi add pada views.py yang
   isinya kurang lebih sama dengan fungsi add_task yang telah dibuat sebelumnya kemudian saya membuat url baru bernama todolist/add, todolist/add ini nantinya akan
   digunakan pada script di todolist.html. Kemudian di bagian script pada todolist.html akan dibuat 3 fungsi yaitu getTodolist, refreshTodolist, dan addTodolist. 
   getTodolist akan mengambil data dari show_json, refreshTodolist akan me-refresh todolist secara asinkronus, dan addTodolist akan digunakan untuk menambahkan
   data pada todolist. addTodolist akan berjalankan ketika kita memencet tombol Submit Task pada modal Add Task, setelah dipencet maka akan menjalankan                    refreshTodolist.
