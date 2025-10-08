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

Tugas 5.
1. Urutan prioritas pengambilan CSS selector (Specificity)

Ringkasan singkat Urutan prioritas CSS ditentukan oleh specificity (spesifisitas) dan urutan sumber (source order). Secara umum dari prioritas tertinggi ke terendah:

Deklarasi !important (dengan catatan aturan tambahan tentang user/author stylesheet).

Gaya inline dalam atribut HTML (style="...").

Selector dengan ID (#id).

Selector kelas, atribut, dan pseudo-class (.class, [attr], :hover).

Selector elemen dan pseudo-element (div, p, ::after).

Selector universal (*) dan aturan dari user-agent (browser) adalah yang paling rendah.

2.Perangkat beragam: pengguna mengakses web dari ponsel, tablet, laptop, TV, dsb. Layout harus beradaptasi.

Pengalaman pengguna (UX): konten yang tidak tersusun untuk ukuran layar membuat pengguna frustrasi (zoom, scroll horizontal, atau elemen yang terlalu kecil).

SEO & jangkauan: mesin pencari (Google) memberi prioritas pada pengalaman mobile-friendly.

Efisiensi pengembangan: desain responsif yang baik mengurangi kebutuhan dua versi terpisah (desktop vs mobile).

Aksesibilitas & inklusivitas: layout responsif lebih mudah dioptimalkan untuk pembaca layar dan pengguna dengan kebutuhan khusus.

3. Margin: ruang di luar border. Mempengaruhi jarak antar elemen. Tidak berwarna (transparan), dan dapat collapse (pada elemen block-berturut-turut, margin vertikal bisa bergabung).

Border: garis/bingkai di antara padding dan margin. Mempunya gaya, lebar, warna.

Padding: ruang antara content dan border. Menaikkan ukuran kotak jika box-sizing: content-box.
<div class="box">Isi</div>
/* reset box-sizing rekomendasi */
*, *::before, *::after { box-sizing: border-box; }


.box {
margin: 24px; /* ruang luar */
padding: 16px; /* ruang di dalam */
border: 2px solid #333; /* bingkai */
background: #fafafa;
}

4. Flexbox (Flexible Box)

Satu dimensi: mengatur layout sepanjang satu sumbu (baris atau kolom).

Container: display: flex; atau display: inline-flex;.

Properti penting di container: flex-direction, justify-content, align-items, flex-wrap, gap.

Properti penting di item: flex-grow, flex-shrink, flex-basis, order, align-self.

Kegunaan: membuat header, navbar, centering vertikal/horizontal, flexible card list, responsive items yang mengisi ruang.

5. Nambah tailwind. Nambah fitur edit,hapus product , dan navigation bar. Nambah static (Css dan no-products image) lalu styling CSS nya.

Tugas 6.
1. Synchronous = Browser mengirim request ke server dan menunggu sampai server membalas sebelum bisa melakukan hal lain, Biasanya menyebabkan reload penuh pada halaman, Form login biasa tanpa JavaScript.
	Asynchronous = Browser bisa melanjutkan aktivitas lain (seperti interaksi UI) sambil menunggu respon dari server, Tidak perlu reload seluruh halaman, hanya bagian tertentu yang diperbaru, Fetch API, jQuery AJAX, atau XMLHttpRequest pada login dengan toast.
	
2. User mengisi form dan klik Submit.

JavaScript (AJAX) menangkap event itu, lalu mengirim HTTP request ke Django view (biasanya pakai fetch() dengan header X-Requested-With: XMLHttpRequest).

Django view memproses data seperti biasa (validasi, autentikasi, CRUD, dll).

Jika request-nya AJAX, Django mengembalikan JsonResponse berisi hasil (misalnya { success: True, redirect: "/main/" }).

JavaScript di browser menerima JSON itu dan menampilkan hasil tanpa reload, seperti menampilkan toast atau mengganti isi halaman.

3. User mengisi form dan klik Submit.

JavaScript (AJAX) menangkap event itu, lalu mengirim HTTP request ke Django view (biasanya pakai fetch() dengan header X-Requested-With: XMLHttpRequest).

Django view memproses data seperti biasa (validasi, autentikasi, CRUD, dll).

Jika request-nya AJAX, Django mengembalikan JsonResponse berisi hasil (misalnya { success: True, redirect: "/main/" }).

JavaScript di browser menerima JSON itu dan menampilkan hasil tanpa reload, seperti menampilkan toast atau mengganti isi halaman.

4. Gunakan CSRF Token — selalu kirim token csrfmiddlewaretoken pada request POST.

Gunakan HTTPS untuk mencegah pencurian data login.

Validasi data di server (jangan hanya di sisi JavaScript).

Batasi endpoint AJAX hanya menerima POST dan X-Requested-With: XMLHttpRequest.

Gunakan JsonResponse yang aman, tanpa menampilkan data sensitif di respon.

5. Memberi respons instan tanpa reload halaman.

Transisi dan feedback (misalnya toast sukses/gagal) terasa lebih natural dan cepat.

Meningkatkan interaktivitas dan kenyamanan pengguna.

Membuat website terasa seperti aplikasi modern (SPA) walau masih pakai Django template.