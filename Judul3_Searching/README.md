a. Judul Program<br>
Sistem Reservasi Slot Parkir Mall Berbasis Struktur data Sequential Search. <br>
<br>
b. Deskripsi Singkat<br>
Program ini berfungsi sebagai sistem manajemen parkir digital yang memungkinkan pengguna untuk melihat ketersediaan ruang 
parkir secara real-time dan melakukan pengisian slot secara mandiri. Program ini meniru parkir di pusat pembelanjaan, di mana 
pengguna dapat memilih nomor slot yang tersedia selama slot itu tidak terisi dengan kendaraan lain. 
<br>
Dalam pengembangannya, program ini menggunakan struktur data List 1 dimensi dengan menggunakan sequential search untuk 
menjalankan kode tersebut. Program ini berfungsi untuk mengatasi pengguna yang ingin mencari parkir tanpa harus memeriksa
seluruh tempat parkir untuk mencari slot kosong.
<br>
c. Source Code<br>
<img width="1672" height="829" alt="Screenshot 2026-05-09 185848" src="https://github.com/user-attachments/assets/98cf0b47-1735-4cc1-a074-dbbdcea7ac7d" />
<img width="1678" height="207" alt="Screenshot 2026-05-09 190057" src="https://github.com/user-attachments/assets/fe0a216e-a904-4d0a-b594-5c786c22e615" />
penjelasannya perbaris:<br>
Baris 1: Membuat fungsi tampilkan_parkiran dengan parameter list.<br>
Baris 2: Mencetak judul status parkir.<br>
Baris 3: Melakukan perulangan untuk mengecek setiap indeks list.<br>
Baris 4: Mencetak nomor slot dan statusnya secara menyamping.<br>
Baris 5: Mencetak baris baru untuk kerapian.<br>
Baris 6: 
Baris 7: Membuat fungsi proses_parkir untuk mengolah pilihan user.<br>
Baris 8: Mengubah pilihan user menjadi nomor indeks (pilihan - 1).<br>
Baris 9: Memvalidasi apakah nomor slot tersedia dalam daftar.<br>
Baris 10: Mencetak pesan error jika slot tidak ada.<br>
Baris 11: Menghentikan fungsi dengan status gagal (False).<br>
Baris 12: Mengecek (Searching) apakah status slot target adalah "KOSONG".<br>
Baris 13: Mengubah status slot target menjadi "TERISI" (Update data).<br>
Baris 14: Mencetak pesan sukses parkir.<br>
Baris 15: Menghentikan fungsi dengan status sukses (True).<br>
Baris 16: Blok jika slot tidak kosong (sudah terisi).<br>
Baris 17: Mencetak pesan bahwa slot sudah penuh.<br>
Baris 18: Menghentikan fungsi dengan status gagal (False).<br>
Baris 19: 
Baris 20: Membuat fungsi main sebagai pusat program.<br>
Baris 21: Membuat list parkiran_mall sebagai database awal.<br>
Baris 22: Mencetak header nama aplikasi.<br>
Baris 23: 
Baris 24: Memulai perulangan agar program terus berjalan.<br>
Baris 25: Memanggil fungsi untuk menampilkan denah terbaru.<br>
Baris 26: Memulai blok try untuk mencegah error input bukan angka.<br>
Baris 27: Mengambil input angka dari pengguna.<br>
Baris 28: Mengecek jika pengguna memilih angka 0.<br>
Baris 29: Mencetak pesan terima kasih.<br>
Baris 30: Keluar dari perulangan dan menutup program.<br>
Baris 31: Menjalankan fungsi proses parkir dengan input user.<br>
Baris 32: Blok jika terjadi kesalahan tipe data (bukan angka).<br>
Baris 33: Mencetak peringatan agar memasukkan angka saja.<br>
Baris 32: 
Baris 35: Mengecek apakah file dijalankan sebagai program utama.<br>
Baris 36: Memanggil fungsi main() untuk memulai aplikasi.<br>
<br>
outputnya:
<img width="1605" height="354" alt="Screenshot 2026-05-09 194903" src="https://github.com/user-attachments/assets/bc8e4479-3e25-49e9-b673-45ce96af769d" />
