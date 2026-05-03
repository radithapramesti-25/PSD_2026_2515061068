a. Judul Program <br>
Program Manajemen Playlist Lagu Berbasis Single Linked List Terhubung.

b. Deskripsi singkat <br>
Program ini berfungsi sebagai manajemen daftar putar musik sederhana, program ini memungkinkan pengguna menyimpan judul lagu dan nama 
penyanyi secara dinamis. Tidak seperti array statis, program ini memungkinkan penambahan lagu kapan saja sekama memori komputer mencukupi.

Algoritma Single Linked List menggunakan struktur data simpul (Node) di mana setiap lagu menyimpan datanya sendiri dan sebuah penunjuk
(pointer) yang berisi alamat memori lagu berikutnya. Dalam penambahan lagu prinsiputama yang digunakan adalag insert at End, yang berarti 
menyisipkan data baru di ujung antrian dengan menelusuri seluruh daftar hingga menemukan titik yang tidak memiliki sambungan lagi.

c Source Code <br>
<img width="925" height="823" alt="Screenshot 2026-04-28 184852" src="https://github.com/user-attachments/assets/1253c452-fd8f-43d1-af5a-de8b7a20eb5c" />
Baris 1: Mendefinisikan class Node sebagai kerangka dasar untuk setiap elemen (lagu) dalam Linked List.<br>
Baris 2: Inisialisasi fungsi konstruktor yang dijalankan setiap kali ada lagu baru dibuat.<br>
Baris 3: Menyimpan data berupa judul lagu ke dalam atribut self.judul.<br>
Baris 4: Menyimpan data nama penyanyi ke dalam atribut self.penyanyi.<br>
Baris 5: Inisialisasi penunjuk self.next dengan nilai None (penanda bahwa simpul belum terhubung ke lagu lain).<br>
Baris 7: Mendefinisikan class PlaylistLagu untuk mengelola operasi pada seluruh daftar lagu.<br>
Baris 8: Fungsi inisialisasi untuk objek playlist.<br>
Baris 9: Menetapkan atribut self.start sebagai None (menandakan playlist awalnya kosong).<br>
Baris 11: Fungsi tambah_lagu untuk menyisipkan lagu baru di urutan paling akhir.<br>
Baris 12: Membuat objek simpul baru (new_node) dari kelas Node.<br>
Baris 13: Mengecek kondisi apakah playlist masih kosong (self.start is None).<br>
Baris 14: Jika kosong, simpul baru langsung dijadikan simpul pertama.<br>
Baris 15: Blok else jika playlist sudah memiliki isi.<br>
Baris 16: Membuat variabel current yang dimulai dari simpul pertama sebagai alat bantu telusur.<br>
Baris 17: Melakukan perulangan selama simpul saat ini masih memiliki sambungan ke simpul lain.<br>
Baris 18: Memindahkan posisi current ke simpul berikutnya.<br>
Baris 19: Setelah menemukan ujung list, hubungkan simpul terakhir tersebut ke simpul baru.<br>
Baris 20: (Kosong/Spasi kode).<br>
Baris 21: Mencetak pesan konfirmasi ke layar bahwa lagu berhasil ditambahkan.<br>
Baris 23: Fungsi tampilkan_playlist untuk mencetak semua lagu secara berurutan.<br> 
Baris 24: Mengecek apakah playlist kosong.<br>
Baris 25: Jika kosong, tampilkan info bahwa playlist tidak memiliki lagu dan keluar dari fungsi.<br>
Baris 26: Keluar dari fungsi jika kondisi kosong terpenuhi.<br>
Baris 27: (Kosong/Spasi kode).<br>
Baris 28: Mencetak garis pembatas judul playlist.<br>
Baris 29: Memulai penelusuran dari simpul pertama (start).<br>
<img width="818" height="773" alt="Screenshot 2026-04-28 184924" src="https://github.com/user-attachments/assets/2c2cec7e-c0ca-4fa5-9437-081e910428e7" />
Baris 30: Inisialisasi variabel nomor urut.<br>
Baris 31: Melakukan perulangan selama simpul yang dibaca tidak bernilai None.<br>
Baris 32: Mencetak nomor urut, judul lagu, dan penyanyi dari simpul saat ini.<br>
Baris 33: Memindahkan posisi baca ke simpul berikutnya melalui pointer next.<br>
Baris 34: Menambah angka pada variabel nomor urut.<br>
Baris 35: Mencetak garis penutup daftar.<br>
Baris 37: Mendefinisikan fungsi main sebagai pusat kendali interaksi pengguna.<br>
Baris 38: Membuat instance (objek) my_playlist dari kelas PlaylistLagu.<br>
Baris 39: (Kosong/Spasi kode).<br>
Baris 40: Mencetak kalimat selamat datang.<br>
Baris 41: (Kosong/Spasi kode).<br>
Baris 42: Memulai perulangan while True agar menu terus muncul selama program berjalan.<br>
Baris 43: Mencetak teks label menu.<br>
Baris 44: Mencetak pilihan menu 1 (Tambah).<br>
Baris 45: Mencetak pilihan menu 2 (Lihat).<br>
Baris 46: Mencetak pilihan menu 3 (Keluar).<br>
Baris 47: (Kosong/Spasi kode).<br>
Baris 48: Mengambil input pilihan angka dari pengguna.<br>
Baris 49: (Kosong/Spasi kode).<br>
Baris 50: Percabangan jika pengguna memilih menu '1'.<br>
Baris 51: Meminta input judul lagu.<br>
Baris 52: Meminta input nama penyanyi.<br>
Baris 53: Memanggil fungsi tambah_lagu dengan data yang sudah diinput.<br>
Baris 54: (Kosong/Spasi kode).<br>
Baris 55: Percabangan jika pengguna memilih menu '2'.<br>
Baris 56: Memanggil fungsi tampilkan_playlist.<br>
<img width="803" height="259" alt="Screenshot 2026-04-28 185010" src="https://github.com/user-attachments/assets/9b9337b6-54d5-46cb-97cd-18dd0480523b" />
Baris 57: (Kosong/Spasi kode).<br>
Baris 58: Percabangan jika pengguna memilih menu '3'.<br>
Baris 59: Mencetak pesan penutup program.<br>
Baris 60: Perintah break untuk menghentikan perulangan dan menutup aplikasi.<br>
Baris 61: (Kosong/Spasi kode).<br>
Baris 62: Blok else jika pengguna memasukkan angka selain 1, 2, atau 3.<br>
Baris 64: Pengecekan apakah script dijalankan secara langsung sebagai program utama.<br>
Baris 65: Memanggil fungsi main() untuk memulai eksekusi seluruh rangkaian kode.<br>

Output program<br>
<img width="638" height="799" alt="Screenshot 2026-04-28 191412" src="https://github.com/user-attachments/assets/f50c388a-92e1-41ec-8751-ac56687f7764" />
Inisialisasi & Menu: Saat program dijalankan, sistem menampilkan Menu Utama (Tambah, Lihat, Keluar). Pada titik ini, Linked List telah dibuat namun masih kosong.<br>
Input Data (Proses Tambah): Ketika kamu memilih angka 1, program meminta input judul (Sial) dan penyanyi (Mahalini). Muncul notifikasi sukses yang menandakan sebuah simpul (Node) baru telah berhasil dibuat dan alamatnya disimpan oleh pointer start.<br>
Tampilan Playlist (Proses Traversal): Saat memilih angka 2, program melakukan penelusuran dari simpul pertama hingga akhir. Sistem mencetak daftar lagu secara rapi dengan nomor urut, membuktikan bahwa pointer antarsimpul telah terhubung dengan benar.<br>
Terminasi (Proses Keluar): Saat memilih angka 3, program mencetak pesan penutup dan menghentikan perulangan, menandakan aplikasi ditutup tanpa error.<br>
