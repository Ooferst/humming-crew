Mengimplementasikan checklist:
Pertama saya menginstall django untuk folder barunya dengan command python -m venv env, lalu saya mengaktifkan virtual environment dengan command env\Scripts\activate, lalu saya menginstall requirements.txt yang ada tutorial lalu saya membuat projek django baru.
Untuk membuat aplikasi dengan nama main pada proyek saya menggunakan command python manage.py startapp main.
Untuk routing pada proyek pertama saya membuat urls.py lalu mengcopy+paste yang ada di tutorial 0, yaitu menginput kode berikut:
	from django.urls import path, include
	urlpatterns = [
		path('', include('main.urls')),
	]
untuk atribut saya menambahkannya di dalam models.py dalam direktori main dengan cara mengambil template yang ada di tutorial 0 lalu menambahkan atribut lain yang ada pada sigma sportswear (nama, harga, description, thumbnail, rating, size).
untuk views.py saya hanya menggunakan template lama lalu menggantikan footballnews dengan {{app_name}}.
untuk urls.py yang berada di main saya juga menggunakan yang ada di tutorial 1 yaitu
	from django.urls import path
	from main.views import show_main

	app_name = 'main'

	urlpatterns = [
		path('', show_main, name='show_main'),
	]
untuk melakukan deployment ke PWS pertama saya buat project di website pacil lalu saya menginput cmd yang disuruh disana (Tidak saya berikan karena bersifat private). Lalu saya meng add ke github terus commit lalu push origin master dan pws master.

Client -> urls.py -> Template -> Response
			|			|
			|			|-- -- -- --<
			> views.py	-> context(data)
			|
			> models.py
urls.py: peta jalan. Menentukan URL mana memanggil fungsi apa.
views.py: logika atau otaknya. Mengatur apa yang dilakukan.
models.py: penghubung data. Mengakses database
HTML(template): tampilan. Data views.py ditampilkan pada web

Peran settings.py dalam django:
File settings.py berfungsi sebagai pusat konfigurasi proyek Django. Isinya mengatur banyak hal penting, settings.py itu otak konfigurasi tanpa file ini, Django tidak tahu bagaimana aplikasi harus dijalankan.

Migrasi dalam Django adalah cara untuk menerapkan perubahan pada model ke database. Django menggunakan sistem migrasi berbasis file, di mana setiap perubahan pada model menghasilkan file migrasi. File ini mencatat apa saja yang perlu diubah pada struktur database, seperti menambahkan tabel baru, menghapus kolom, atau memodifikasi tipe data.
Cara kerja ialah membuat model lalu menjalankan cmd nya yaitu manage.py makemigrations untuk menghasilkan file migrasi yang berisi perubahan. Setelah itu menjalankan manage.py migrate untuk menerapkan perubahan ke database.

Karena framework django lebih gampang, lebih stabil dan tidak rumit jadi intinya best practice lah menggunakan django untuk pemula.

Untuk feedback, menurut saya sudah bagus.