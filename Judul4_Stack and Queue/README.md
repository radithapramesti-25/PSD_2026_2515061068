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
Baris 51: Memulai perulangan while True agar menu tampil secara berulang.<br>
Baris 52: Mencetak pilihan Menu 1 untuk operasi Push (Masuk Barang).<br>
Baris 53: (Baris Kosong)<br>
Baris 54: Mencetak pilihan Menu 2 untuk operasi Pop (Ambil Barang).<br>
Baris 55: (Baris Kosong)<br>
Baris 56: Mencetak pilihan Menu 3 untuk operasi Peek (Lihat Barang Teratas).<br>
Baris 57: Mencetak pilihan Menu 4 untuk operasi Display (Lihat Semua).<br>
Baris 58: Mencetak pilihan Menu 5 untuk mengakhiri program.<br>
Baris 59: Mengambil angka pilihan menu yang diketikkan oleh user.<br>
Baris 60: Menjalankan logika if untuk memproses Pilihan 1 (Push).<br>
Baris 61: Meminta user mengetikkan nama barang yang akan dimasukkan.<br>
Baris 62: Memanggil fungsi push dengan data nama barang tersebut.<br>
Baris 63: (Baris Kosong)<br>
Baris 64: Menjalankan logika elif untuk memproses Pilihan 2 (Pop).<br>
Baris 65: (Baris Kosong)<br>
Baris 66: Memanggil fungsi pop milik objek gudang untuk mengeluarkan barang.<br>
Baris 67: Menjalankan logika elif untuk memproses Pilihan 3 (Peek).<br>
Baris 68: Memanggil fungsi peek untuk melihat barang di posisi teratas.<br>
Baris 69: Menjalankan logika elif untuk memproses Pilihan 4 (Display).<br>
Baris 70: Memanggil fungsi display untuk menampilkan denah gudang.<br>
Baris 71: Menjalankan logika elif untuk memproses Pilihan 5 (Keluar).<br>
Baris 72: Mencetak pesan penutup dan terima kasih kepada pengguna.<br>
Baris 73: Menggunakan perintah break untuk memutus perulangan menu.<br>
Baris 74: Blok else terakhir jika pilihan menu tidak ada di daftar (1-5).<br>
Baris 75: Mencetak peringatan bahwa pilihan yang dimasukkan user salah.<br>
Baris 76: Menutup blok try dengan except ValueError (salah tipe data).<br>
Baris 77: Mencetak pesan bahwa input kapasitas harus berupa angka.<br>
Baris 78: Baris tambahan untuk memisahkan logika utama dengan eksekusi.<br>
Baris 79: Mengecek apakah file Python ini dijalankan sebagai skrip utama.<br>
Baris 80: (Baris Kosong)<br>
Baris 81: Memanggil fungsi main() untuk mulai menjalankan aplikasi.<br>
Baris 82: Baris akhir program sebagai tanda selesainya seluruh instruksi.<br>
