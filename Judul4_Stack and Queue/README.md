a. judul program<br>
Sistem Manajemen Logistik Gudang Otomatis Berbasis Stack (LIFO).<br>
<br>
b. Deskripsi singkat<br>
Program ini bertujuan untuk menstimulasikan sistem penyimpanan barang digudang otomatis, yang memiliki satu 
pintu untuk masuk dan keluar barang. fungsi utama program adalah untuk memantau barang yang masuk dan 
mengambil barang dengan urutan yang benar, serta mencegah lorong gudang mengalami overload(kapasitas maksimal).<br>
<br>
Struktur data Stack (Tumpukan) dengan prinsip LIFO (Last In, First Out) digunakan. Dalam kasus ini, objek yang 
terakhir dimasukkan ke dalam lorong adalah objek yang harus dikeluarkan terlebih dahulu agar petugas dapat 
mengakses objek di bawahnya. Implementasi menyimpan data barang secara sekuensial menggunakan representasi 
Array (List dalam Python).<br>
<br>
c. source kode<br>
<img width="1700" height="868" alt="Screenshot 2026-05-16 162433" src="https://github.com/user-attachments/assets/9900bed7-5be8-42fd-9f5b-171700f020a7" />
<img width="1694" height="802" alt="Screenshot 2026-05-16 162526" src="https://github.com/user-attachments/assets/ea42e5a7-25e7-428c-9aad-162817a4b5af" />
<img width="1695" height="722" alt="Screenshot 2026-05-16 162558" src="https://github.com/user-attachments/assets/9adef99e-1e33-4f71-ab81-1e1a1cc85189" />
penjelasannya perbaris<br>
Baris 1: Membuat class StackGudang sebagai cetakan utama struktur data tumpukan.<br>
Baris 2: Mendefinisikan fungsi __init__ untuk menginisialisasi objek gudang baru.<br>
Baris 3: Menyimpan batas maksimal daya tampung gudang ke dalam variabel self.MAX.<br>
Baris 4: Membuat list self.barang berisi slot kosong (None) sebanyak kapasitas.<br>
Baris 5: Mengatur self.top_idx ke -1 sebagai penanda tumpukan masih kosong.<br>
Baris 6: (Baris Kosong)<br>
Baris 7: Membuat fungsi is_empty untuk mengecek apakah tidak ada barang di gudang.<br>
Baris 8: Mengembalikan nilai True jika top_idx bernilai -1 (gudang kosong).<br>
Baris 9: (Baris Kosong)<br>
Baris 10: Membuat fungsi is_full untuk mengecek apakah kapasitas sudah maksimal.<br>
Baris 11: Mengembalikan nilai True jika top_idx sudah mencapai indeks terakhir.<br>
Baris 12: (Baris Kosong)<br>
Baris 13: Membuat fungsi push untuk memasukkan barang baru ke tumpukan.<br>
Baris 14: Melakukan validasi menggunakan is_full agar tidak terjadi luapan data.<br>
Baris 15: Mencetak pesan error jika barang gagal masuk karena gudang penuh.<br>
Baris 16: Blok else yang berjalan jika gudang masih memiliki ruang.<br>
Baris 17: Menaikkan nilai top_idx sebesar 1 untuk menunjuk slot di atasnya.<br>
Baris 18: Memasukkan nama barang ke dalam list sesuai indeks top_idx terbaru.<br>
Baris 19: Mencetak konfirmasi bahwa barang berhasil disimpan di gudang.<br>
Baris 20: (Baris Kosong)<br>
Baris 21: Membuat fungsi pop untuk mengambil barang teratas (paling luar).<br>
Baris 22: Melakukan validasi menggunakan is_empty untuk mencegah pengambilan dari gudang kosong.<br>
Baris 23: Mencetak pesan peringatan jika tidak ada barang yang bisa diambil.<br>
Baris 24: Mengembalikan nilai None sebagai tanda operasi pengambilan gagal.<br>
Baris 25: Blok else yang berjalan jika terdeteksi ada barang di dalam gudang.<br>
Baris 26: Menyimpan data barang teratas ke dalam variabel sementara barang_diambil.<br>
Baris 27: Menurunkan nilai top_idx sebesar 1 (menghapus akses ke barang lama).<br>
Baris 28: Mencetak informasi nama barang yang berhasil dikeluarkan dari sistem.<br>
Baris 29: Mengembalikan nama barang yang diambil kepada pengguna.<br>
Baris 30: (Baris Kosong)<br>
Baris 31: Membuat fungsi peek untuk melihat barang di tumpukan teratas tanpa mengambilnya.<br>
Baris 32: Validasi jika tumpukan kosong, maka tidak ada yang bisa diintip.<br>
Baris 33: Mencetak status bahwa saat ini gudang tidak berisi barang.<br>
Baris 34: Blok else jika gudang berisi minimal satu barang.<br>
Baris 35: Menampilkan nama barang yang berada pada posisi indeks top_idx.<br>
Baris 36: (Baris Kosong)<br>
Baris 37: Membuat fungsi display untuk memvisualisasikan seluruh lorong gudang.<br>
Baris 38: Mengecek apakah gudang kosong sebelum memulai proses cetak.<br>
Baris 39: Mencetak judul atau header tabel tumpukan barang.<br>
Baris 40: Melakukan perulangan mundur (range) dari posisi teratas ke terbawah.<br>
Baris 41: Mencetak format kotak tumpukan berisi nama barang dan indeksnya.<br>
Baris 42: Mencetak garis penutup di bawah tumpukan untuk estetika.<br>
Baris 43: Blok else jika gudang kosong saat perintah display dipanggil.<br>
Baris 44: Mencetak pesan informasi bahwa tidak ada data untuk ditampilkan.<br>
Baris 45: (Baris Kosong)<br>
Baris 46: Membuat fungsi main sebagai pusat kendali seluruh aktivitas program.<br>
Baris 47: Mencetak header selamat datang ke sistem gudang otomatis.<br>
Baris 48: Memulai blok try untuk menangani kesalahan input user (bukan angka).<br>
Baris 49: Mengambil input kapasitas maksimal dan mengubahnya ke tipe data integer.<br>
Baris 50: Membuat objek gudang berdasarkan class StackGudang.<br>
Baris 51: Mengatur nilai variabel kapasitas menjadi 5 sebagai nilai standar (default).
Baris 52: Mencetak pesan ke layar untuk memberi tahu pengguna bahwa input sebelumnya tidak sah, sehingga sistem otomatis menggunakan kapasitas default yaitu 5.<br>
Baris 53:  (Baris Kosong)<br>
Baris 54: Membuat objek baru bernama gudang dari class StackGudang dengan memasukkan nilai kapasitas (yaitu 5) sebagai batas maksimal daya tampung tumpukan tersebut.<br>
Baris 55: (Baris Kosong)<br>
Baris 56: Memulai perulangan while True agar menu tampil secara berulang.<br>
Baris 57: mencetak tampilan menu operasi.<br>
Baris 58: Mencetak pilihan Menu 1 untuk operasi Push (Masuk Barang).<br>
Baris 59: Mencetak pilihan Menu 2 untuk operasi Pop (Ambil Barang).<br>
Baris 60: Mencetak pilihan Menu 3 untuk operasi Peek (Lihat Barang Teratas).<br>
Baris 61: Mencetak pilihan Menu 4 untuk operasi Display (Lihat Semua).<br>
Baris 62: Mencetak pilihan Menu 5 untuk mengakhiri program.<br>
Baris 66: Memeriksa apakah pengguna memilih menu nomor '1' (biasanya untuk menambah barang).<br>
Baris 67: Mengambil input teks dari pengguna berupa nama barang dan menyimpannya ke dalam variabel nama.<br>
Baris 68: Memasukkan (push) variabel nama barang tersebut ke dalam tumpukan gudang.<br>
Baris 69: Memeriksa apakah pengguna memilih menu nomor '2'.<br>
Baris 70: Menghapus atau mengeluarkan (pop) barang yang berada di posisi paling atas dari tumpukan gudang.<br>
Baris 71: Memeriksa apakah pengguna memilih menu nomor '3'.<br>
Baris 72: Melihat (peek) barang yang berada di posisi paling atas tumpukan tanpa menghapusnya.<br>
Baris 73: Memeriksa apakah pengguna memilih menu nomor '4'.<br>
Baris 74: Menampilkan (display) seluruh daftar barang yang ada di dalam tumpukan gudang.<br>
Baris 75: Memeriksa apakah pengguna memilih menu nomor '5' (untuk keluar).<br>
Baris 76: Mencetak pesan penutup ke layar sebagai tanda program selesai digunakan.<br>
Baris 77: Menghentikan paksa perulangan (Loop seperti while), sehingga program utama berhenti berjalan.<br>
Baris 78: Blok alternatif jika input pilihan yang dimasukkan pengguna tidak ada di angka '1' sampai '5'.<br>
Baris 79: Mencetak pesan peringatan bahwa input pengguna tidak valid.<br>
Baris 80: (Baris Kosong)<br>
Baris 81: Memanggil fungsi main() untuk mulai menjalankan aplikasi.<br>
Baris 82: Baris akhir program sebagai tanda selesainya seluruh instruksi.<br>
<br>
Outuputnya:<br>
<img width="1648" height="873" alt="Screenshot 2026-05-16 210739" src="https://github.com/user-attachments/assets/db449ba4-1ab1-418e-8996-39cc34f5e7bf" />
<img width="1643" height="858" alt="Screenshot 2026-05-16 210807" src="https://github.com/user-attachments/assets/0baeb973-9e58-457d-9494-b2f6a6490aa7" />
<img width="1649" height="874" alt="Screenshot 2026-05-16 210831" src="https://github.com/user-attachments/assets/219f747e-b92c-4a95-aee1-4a7fda368aca" />
<img width="1637" height="476" alt="Screenshot 2026-05-16 210854" src="https://github.com/user-attachments/assets/88ac4687-7135-4c2e-8720-6c071048654d" />
<br>
penjelasannya:<br>
1. Memasukkan Barang (Push)<br>
Setiap kali kita memasukkan barang, barang tersebut akan diletakkan di posisi paling atas dari tumpukan yang sudah ada. Karena kapasitas gudang hanya 5, maka barang ke-6 (garpu) tidak bisa masuk karena gudang sudah tidak punya ruang lagi.
<br>
2. Melihat Tumpukan (Display)<br>
Saat kita melihat isi gudang, kamu akan melihat daftar barang dari yang paling atas ke bawah. Barang yang baru saja kamu masukkan (rendang) akan terlihat di nomor urut tertinggi, sementara barang pertama yang dimasukkan (obat) berada di dasar tumpukan.<br>
<br>
3. Mengambil Barang (Pop)<br>
mengambil barang yang berada di posisi paling atas terlebih dahulu. Itulah sebabnya saat "Ambil Barang" dipilih, rendang yang keluar lebih dulu, bukan obat.<br>
<br>
4. Keluar dari Sistem<br>
Setelah selesai dengan semuanya (menambah, melihat, atau mengambil), memilih menu keluar untuk mematikan program.<br>
<br>
link youtube:<br>
https://youtu.be/51liYVaG9iE
