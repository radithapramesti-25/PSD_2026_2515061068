a. Judul Program <br>
Program Merapikan Uang Kertas di Kasir menggunakan insertion sort <br>
<br>
b. Deskripsi singkat <br>
Program ini berfungsi untuk mengurutkan tumpukan nominal uang kertas yang tidak teratur menjadi teratur dari 
nilai terkecil ke nilai terbesar (Ascending). Hal ini bertujuan untuk membantu kasir dalam menghitung total uang 
atau mengatur laci kasir dengan sistematis untuk mengurangi kesalahan transaksi.<br>
Insertion Sort adalah algoritma struktur data yang digunakan untuk membagi daftar menjadi bagian yang belum terurut menjadi
terurut. Setiap elemen dari bagian yang belum terurut "disisipkan" ke posisi yang sudah terurut, mirip dengan cara seseorang
mengurutkan kartu dengan tangan.
<br>

c. Source Code & Penjelasan Logika<br>
<img width="1715" height="853" alt="Screenshot 2026-05-03 144210" src="https://github.com/user-attachments/assets/747ff662-afda-4d21-a391-5d9ab695d6ef" />
<img width="1707" height="380" alt="Screenshot 2026-05-03 144235" src="https://github.com/user-attachments/assets/5da5b00b-c14e-4bb3-9a92-85d721088037" />
Penjelasan Logika Baris demi Baris:<br>
Baris 1: Komentar judul fungsi sebagai identitas algoritma Insertion Sort.<br>
Baris 2: Deklarasi fungsi insertion_sort_uang dengan parameter list uang dan jumlahnya.<br>
Baris 3: Perulangan utama untuk mengecek uang mulai dari lembar kedua hingga akhir.<br>
Baris 4: Komentar mengenai proses pengambilan elemen untuk dibandingkan.<br>
Baris 5: Menyimpan nominal uang yang sedang dicek ke variabel sementara (temp).<br>
Baris 6: Menentukan indeks j (uang di sebelah kiri temp) sebagai pembanding.<br>
Baris 7: (Kosong) Ruang jeda untuk keterbacaan kode.<br>
Baris 8: Komentar mengenai logika penggeseran nominal yang lebih besar.<br>
Baris 9: Perulangan while untuk mencari posisi penyisipan yang tepat.<br>
Baris 10: Syarat geser: selama uang di kiri lebih besar dari uang di tangan (temp).<br> 
Baris 11: Menggeser uang yang lebih besar ke posisi kanan.<br>
Baris 12: Mundur ke indeks sebelumnya untuk pengecekan lebih lanjut.<br> 
Baris 13: Menyisipkan uang temp ke posisi yang sudah benar.<br>
Baris 14: (Kosong/Indentasi keluar) Penanda akhir dari blok fungsi algoritma.<br>
Baris 15: Deklarasi fungsi main() sebagai pusat kendali program.<br>
Baris 16: Mencetak judul besar program di terminal kasir.<br>
Baris 17: Membuka blok try untuk menangkap kesalahan input angka.<br>
Baris 18: Mengambil input jumlah lembar uang dari kasir.<br>
Baris 19: Blok except jika kasir menginput selain angka (misal: huruf).<br> 
Baris 20: Pesan peringatan bahwa input harus berupa angka bulat.<br>
Baris 21: Menghentikan program jika input jumlah lembar tidak valid.<br>
Baris 22: (Kosong) Jeda antar logika input.<br>
Baris 23: Inisialisasi list uang_kertas sebagai wadah penyimpanan data.<br>
Baris 24: Mencetak instruksi pengisian nominal untuk kasir.<br>
Baris 25: Perulangan untuk meminta input nominal sebanyak jumlah lembar.<br>
Baris 26: Loop while True untuk memvalidasi setiap nominal satu per satu.<br>
Baris 27: Blok try untuk memastikan nominal adalah angka integer.<br>
Baris 28: Menyimpan input nominal ke dalam list menggunakan .append().<br> 
Baris 29: Keluar dari loop validasi jika input nominal sudah benar.<br>
Baris 30: Menangkap error jika nominal yang diinput bukan angka.<br>
Baris 31: Pesan edukasi agar kasir memasukkan angka nominal yang valid.<br> 
Baris 32: (Kosong/Print Jeda) Memberikan jarak visual sebelum menampilkan hasil proses.<br>
Baris 33: Komentar penanda penampilan kondisi data awal.<br>
Baris 34: Mencetak daftar uang yang masih acak/berantakan.<br>
Baris 35: (Kosong) Jeda sebelum pemanggilan fungsi sorting.<br>
Baris 36: Memanggil fungsi insertion_sort_uang untuk merapikan data.<br>
Baris 37: (Kosong) Jeda sebelum menampilkan hasil akhir.<br>
Baris 38: Mencetak notifikasi bahwa proses merapikan telah selesai.<br> 
Baris 39: Mencetak judul untuk daftar hasil uang yang sudah rapi.<br>
Baris 40: Perulangan untuk mengakses setiap uang yang sudah terurut.<br> 
Baris 41: Mencetak nominal dengan format mata uang "Rp" secara berjejer.<br>
Baris 42: (Kosong) Jeda estetika di akhir output.<br>
Baris 43: Menjalankan fungsi main() saat script dieksekusi secara langsung.<br>
