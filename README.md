1. Karena backend perlu menyediakan data untuk konsumen secara formatted (xml/json) supaya sistem dapat berkomunikasi.
2. JSON: Lebih ringkas, compatible dengan JavaScript. XML: Lebih mendukung struktur dokumen yang kompleks, attributes, dan lain lain.
	Kesimpulan: JSON lebih populer karena sederhana dan mudah dipakai.
3. is_valid() menjalankakn semua validator dan akan mengembalikan False jika error. Kita butuh is_valid() supaya dapat mencegah penyimpanan data tidak valid.
4. tanpa ada csrf token penyerangan bisa dilakukan dari domain lain.
5. Pertama saya mengimplementasi skeleton lalu menaroh kode baru ke dalam settings.py untuk templates/skeletonnya
	Lalu saya mengubah template lama (main) supaya dapat lebih enak dilihat dan lebih banyak informasi yang didapatkan.
	Lalu saya menambahkan 2 template lagi untuk membuat produk nya dan menampilkan detail/deskripsi dari produknya.
	Lalu saya membuat kode untuk mengembalikan data dalam bentuk XMl dan json serta juga by id.
	Lalu saya mengetesnya menggunakan Postman dan akhirnya saya mengumpulkan tugas ini.
6. Untuk feedback saya sendiri sih masih sama, sudah cukup bagus.
7. Gambar: https://drive.google.com/drive/folders/1qdiujwL7zteKkYBCJxjjNlPN2SSay5Wx?usp=sharing

Tugas 4.

1.AuthenticationForm adalah form bawaan Django (ada di django.contrib.auth.forms) yang digunakan untuk login user.
 -Kelebihan: Otomatis melakukan validasi, Mengurangi bug, Bisa langsung dipakai, Sudah terintegrasi.
 -Kekurangan: Field bawaan terbatas, tampilan basic.
 
2.Autentikasi = Proses memverifikasi user, Implementasi: Django menyediakan django.contrib.auth, AuthenticationForm, authenticate(), dan login()
  Otorisasi = Proses menentukan hak akses user, Implementasi:Django punya sistem permissions & groups: @login_required, hanya user login yang bisa akses. @permission_required('app.permission_name'), cek hak akses tertentu. request.user.is_staff / is_superuser, kontrol role user.
   
3.Kelebihan & kekurangan cookies: Mudah digunakan, Bisa dipakai lintas request tanpa serverside storage, Lebih rentant terhadap manipulasi, batas ukuran, keamanan jelek.
  Kelebihan & kekurangan session: Lebih aman, Bisa menyimpan lebih banyak, Django mendukung berbagai backend session, membutuhkan storage server, lebih berat daripada cookie.
4.Tidak sepenuhnya aman, cookies bisa dicuti/dimanipulasi.
  Django menangani dengan cara: HttpOnly=True,Secure=True,CSRF protection dan lainnya.
5.Tambahkan regsiter, login, ya sama dengan tugas kemaren saya ngedit MVT dan urls. Lalu saya mencoba websitenya dan bisa.