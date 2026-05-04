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
Baris 1: Komentar judul program yang menjelaskan tujuan kode secara keseluruhan.<br>
Baris 2: Mendefinisikan fungsi insertion_sort_uang dengan parameter arr (list uang) dan n (jumlah lembar).<br>
Baris 3: Perulangan for dimulai dari indeks ke-1 (lembar kedua) hingga terakhir, karena lembar pertama dianggap sudah terurut sementara.<br>
Baris 4: Mengambil nilai nominal uang pada posisi i dan menyimpannya di variabel temp.<br>
Baris 5: Menentukan variabel j sebagai penunjuk posisi satu tingkat di sebelah kiri i.<br>
Baris 6: (Baris kosong/Spasi) Digunakan untuk memisahkan inisialisasi variabel dengan logika perbandingan.<br>
Baris 7: Perulangan while dimulai untuk membandingkan temp dengan uang-uang di sisi kiri.Syarat perulangan: selama indeks j belum habis dan nominal di arr[j] lebih besar dari temp.<br>
Baris 8: Menggeser nominal uang yang lebih besar ke kanan satu posisi (j + 1) untuk membuka celah penyisipan.<br>
Baris 9: Mengurangi nilai j untuk terus mengecek posisi uang lebih jauh ke arah kiri.<br>
Baris 10: Menyisipkan nilai temp ke posisi yang tepat setelah tidak ada lagi uang yang lebih besar di kirinya.<br>
Baris 11: (Baris kosong/Spasi) Digunakan untuk memisahkan inisialisasi variabel dengan logika perbandingan.<br>
Baris 12: Mendefinisikan fungsi main() sebagai pusat kendali jalannya program.<br>
Baris 13: Mencetak judul besar program ke layar terminal.<br>
Baris 14: Membuka blok try untuk mengantisipasi kesalahan input jumlah lembar uang.<br>
Baris 15: Mengambil input jumlah lembar dari pengguna dan mengubahnya menjadi integer.<br>
Baris 16: Blok except yang menangkap kesalahan jika pengguna memasukkan selain angka pada jumlah lembar.<br>
Baris 17: Menampilkan pesan peringatan bahwa input tidak valid.<br>
Baris 18: Menghentikan fungsi dengan return jika terjadi kesalahan input fatal.<br>
Baris 19: (Baris kosong/Spasi) Jeda pemisah antar blok logika input.<br>
Baris 20: Inisialisasi list kosong uang_kertas untuk menampung data nominal.<br>
Baris 21: Mencetak instruksi cara memasukkan nominal uang.<br>
Baris 22: Perulangan for untuk meminta input nominal sebanyak n kali.<br>
Baris 23: Loop while True dimulai untuk memastikan setiap nominal yang dimasukkan valid sebelum lanjut ke lembar berikutnya.<br>
Baris 24: Blok try untuk memvalidasi setiap input nominal lembar uang.<br>
Baris 25: Mengambil input nominal per lembar berdasarkan urutan ke-i+1.<br>
Baris 26: Menambahkan nominal yang valid ke dalam list uang_kertas menggunakan .append().<br>
Baris 27: Keluar dari while True (break) karena input nominal lembar tersebut sudah benar.<br>
Baris 28: Blok except untuk menangkap kesalahan jika nominal bukan berupa angka.<br>
Baris 30: Menampilkan pesan kesalahan khusus untuk nominal uang.<br>
Baris 30: (Baris kosong/Spasi) Jeda sebelum menampilkan status data awal.<br>
Baris 31: Mencetak daftar nominal uang yang masih dalam kondisi acak.<br>
Baris 32: Mencetak daftar nominal uang yang masih dalam kondisi acak.<br>
Baris 33: Komentar penjelas bahwa tahap selanjutnya adalah pemanggilan fungsi pengurutan.<br>
Baris 34: Mengeksekusi fungsi insertion_sort_uang untuk merapikan isi list uang_kertas.<br>
Baris 35: (Baris kosong/Spasi) Jeda visual setelah proses pengurutan.<br>
Baris 36: Mencetak informasi bahwa proses merapikan telah selesai dilakukan.<br>
Baris 37: Mencetak label untuk hasil akhir pengurutan.<br>
Baris 38: Perulangan for untuk mengakses setiap nominal uang yang kini sudah terurut.<br>
Baris 39: Mencetak nominal uang dengan format "Rp" secara menyamping menggunakan end=" ".<br>
Baris 40: mencetak uang yang sudah dirapihkan.<br>
Baris 41: Memberikan baris kosong baru di akhir daftar agar tampilan terminal rapi.<br>
Baris 42: Kondisi if __name__ == "__main__": untuk menjalankan program hanya jika file ini dieksekusi langsung.<br>
Baris 43: Memanggil fungsi main() untuk memulai seluruh alur kerja program.<br>
<br>
outputnya:
<img width="1598" height="432" alt="Screenshot 2026-05-04 191146" src="https://github.com/user-attachments/assets/b5a9bde5-23a7-4537-80a5-990f72f3d522" />
Kasir memasukkan jumlah 5 lembar uang. Nominal yang dimasukkan secara bertahap adalah 10000, 20000, 2000, 50000, dan 10000.<br>
Program menampilkan daftar nominal dalam bentuk list sesuai urutan input yang masih acak (berantakan): [10000, 20000, 2000, 50000, 10000].<br>
Program menjalankan fungsi insertion_sort_uang untuk membandingkan dan menggeser posisi uang hingga urut.<br>
Hasil Akhir: Setelah proses merapikan selesai, uang ditampilkan secara berurutan dari nominal terkecil ke terbesar: Rp2000 Rp10000 Rp10000 Rp20000 Rp50000.<br>
