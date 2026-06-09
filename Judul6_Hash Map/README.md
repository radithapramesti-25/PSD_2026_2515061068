a. Judul Program<br>
Aplikasi Manajemen Buku Kontak Ponsel Berbasis Struktur Data Hash Map dengan Metode Separate Chaining.<br>
<br>
b. Deskripsi SingkatProgram Buku Kontak Ponsel ini berfungsi sebagai sistem penyimpanan data digital yang
mensimulasikan pencatatan nomor telepon di dalam sebuah perangkat pintar. Program ini memfasilitasi
pengguna untuk melakukan operasi-operasi fundamental manajemen data secara dinamis, meliputi penambahan
kontak baru (insertion), pencarian nomor telepon berdasarkan nama (searching), pembaruan nomor jika nama
kontak sudah terdaftar (updating), penghapusan kontak (deletion), hingga visualisasi alokasi memori internal penyimpanan.<br>
<br>
Algoritma struktur data yang diterapkan pada program ini adalah Hash Map (Tabel Hash). Guna menangani
fenomena benturan data (collision resolution)—yaitu kondisi di mana dua nama kontak yang berbeda
menghasilkan nilai indeks penyimpanan yang sama—program ini menerapkan metode Separate Chaining.
Melalui metode ini, setiap slot memori pada tabel hash bertindak sebagai penunjuk (head) dari sebuah Singly
Linked List. Setiap kali terjadi collision, kontak baru akan disisipkan ke dalam untaian rantai Linked List di slot
tersebut. Struktur data ini dipilih karena menawarkan efisiensi pencarian yang sangat tinggi dengan kompleksitas
waktu rata-rata mencapai O(1) (waktu konstan).<br>
<br>
c. Source Code & Penjelasan Logika Berbaris<br>
<img width="1672" height="830" alt="Screenshot 2026-06-08 215508" src="https://github.com/user-attachments/assets/094da663-e21e-4a48-a527-2649f12fbbfd" />
<img width="1677" height="799" alt="Screenshot 2026-06-08 215546" src="https://github.com/user-attachments/assets/95b34bcc-8594-4fa7-9ca8-dc3d917b4878" />
<img width="1671" height="777" alt="Screenshot 2026-06-08 215620" src="https://github.com/user-attachments/assets/b940f140-b71c-4b07-91ec-78315ec804fb" />
<img width="1675" height="800" alt="Screenshot 2026-06-08 215645" src="https://github.com/user-attachments/assets/faeb04fa-a1c6-4740-8dac-08e9d8526368" />
<img width="1682" height="145" alt="Screenshot 2026-06-08 215714" src="https://github.com/user-attachments/assets/751eefd4-1d87-4bc6-ab2a-b7154f539386" />
<br>
penjelasan kodingannya perbaris:<br>
Baris 1: Memanggil modul os untuk mengontrol sistem operasi seperti membersihkan layar.<br>
Baris 2: (Baris Kosong)<br>
Baris 3: Membuat class Node sebagai cetakan objek simpul untuk rantai Linked List.<br>
Baris 4: Mendefinisikan fungsi init untuk menginisialisasi atribut awal setiap simpul.<br>
Baris 5: Menyimpan nama kontak yang dimasukkan pengguna ke dalam variabel self.key.<br>
Baris 6: Menyimpan nomor telepon kontak ke dalam variabel self.value.<br>
Baris 7: Mengatur penunjuk self.next bernilai None sebagai ujung rantai simpul.<br>
Baris 8: (Baris Kosong)<br>
Baris 9: Membuat class BukuKontakHashMap sebagai cetakan utama tabel memori hash.<br>
Baris 10: Mendefinisikan fungsi init untuk menentukan ukuran ruang penyimpanan data.<br>
Baris 11: Menyimpan kapasitas maksimal tabel hash ke dalam variabel self.SIZE.<br>
Baris 12: Membuat array self.table berisi slot kosong sebanyak kapasitas memori.<br>
Baris 13: (Baris Kosong)<br>
Baris 14: Membuat fungsi hash_function untuk mengubah nama kontak menjadi indeks angka.<br>
Baris 15: Mengonversi string nama menjadi angka acak yang konsisten menggunakan fungsi hash().<br>
Baris 16: Mengembalikan hasil modulo angka hash dengan kapasitas tabel agar pas dengan nomor slot.<br>
Baris 17: (Baris Kosong)<br>
Baris 18: Membuat fungsi insert untuk menambahkan atau memperbarui data kontak.<br>
Baris 19: Mencari lokasi nomor slot memori berdasarkan nama kontak lewat fungsi hash.<br>
Baris 20: Menunjuk variabel current ke isi data pertama pada slot memori tersebut.<br>
Baris 21: (Baris Kosong)<br>
Baris 22: Memulai perulangan untuk menyusuri rantai kontak selama current tidak kosong.<br>
Baris 23: Mengecek apakah nama kontak yang dicari sudah ada di memori (mengabaikan huruf kapital).<br>
Baris 24: Menimpa nomor telepon lama dengan nomor baru jika nama kontak sudah terdaftar.<br>
Baris 25: Memunculkan pesan teks bahwa nomor telepon berhasil diperbarui di layar.<br>
Baris 26: Menghentikan jalannya fungsi karena proses pembaruan data telah selesai.<br>
Baris 27: Menggeser penunjuk current ke simpul berikutnya di dalam rantai linked list.<br>
Baris 28: (Baris Kosong)<br>
Baris 29: Membuat objek simpul (Node) baru untuk menyimpan nama dan nomor kontak baru.<br>
Baris 30: Menghubungkan pointer next simpul baru ke data kontak yang sudah ada di slot.<br>
Baris 31: Menempatkan simpul baru tersebut di urutan paling depan pada slot memori target.<br>
Baris 32: Memunculkan pesan teks bahwa kontak baru berhasil disimpan di layar.<br>
Baris 33: (Baris Kosong)<br>
Baris 34: Membuat fungsi search untuk mencari nomor telepon berdasarkan nama kontak.<br>
Baris 35: Mencari nomor slot tempat nama kontak tersebut disimpan menggunakan fungsi hash.<br>
Baris 36: Menunjuk variabel current ke isi data pertama pada slot memori hasil hash.<br>
Baris 37: (Baris Kosong)<br>
Baris 38: Memulai perulangan untuk menyusuri isi rantai kontak pada slot memori tersebut.<br>
Baris 39: Mengecek apakah ada simpul kontak yang namanya cocok dengan nama yang dicari.<br>
Baris 40: Mengembalikan seluruh data objek simpul kontak jika nama berhasil ditemukan.<br>
Baris 41: Menggeser penunjuk current ke simpul berikutnya di dalam rantai linked list.<br>
Baris 42: Mengembalikan nilai None jika perulangan selesai dan kontak tidak ditemukan.<br>
Baris 43: (Baris Kosong)<br>
Baris 44: Membuat fungsi remove_key untuk menghapus data kontak berdasarkan nama.<br>
Baris 45: Mencari lokasi nomor slot memori dari nama kontak menggunakan fungsi hash.<br>
Baris 46: Menunjuk variabel current ke isi data pertama pada slot memori target.<br>
Baris 47: Membuat variabel prev bernilai None untuk mencatat simpul sebelum current.<br>
Baris 48: (Baris Kosong)<br>
Baris 49: Memulai perulangan untuk menyusuri rantai kontak guna mencari data yang akan dihapus.<br>
Baris 50: Mengecek apakah nama kontak pada simpul saat ini cocok dengan target hapus.<br>
Baris 51: Memeriksa apakah kontak yang akan dihapus berada di urutan paling depan slot.<br>
Baris 52: Menggeser hulu slot memori ke simpul berikutnya jika kontak terdepan dihapus.<br>
Baris 53: Mengatur pointer simpul sebelumnya agar melompati simpul target jika data di tengah.<br>
Baris 54: Memunculkan pesan teks bahwa data kontak sukses dihapus dari memori ponsel.<br>
Baris 55: Mengembalikan nilai True sebagai penanda operasi penghapusan berhasil.<br>
Baris 56: Menyimpan simpul saat ini ke variabel prev sebelum bergeser maju.<br>
Baris 57: Menggeser penunjuk current ke simpul selanjutnya di dalam rantai linked list.<br>
Baris 58: (Baris Kosong)<br>
Baris 59: Memunculkan pesan teks bahwa nama kontak tidak ditemukan di dalam memori.<br>
Baris 60: Mengembalikan nilai False sebagai penanda operasi penghapusan gagal.<br>
Baris 61: (Baris Kosong)<br>
Baris 62: Membuat fungsi display untuk memvisualisasikan kondisi internal memori tabel hash.<br>
Baris 63: Mencetak garis pembatas atas untuk judul visualisasi memori ke layar terminal.<br>
Baris 64: Melakukan perulangan untuk memeriksa setiap slot dari indeks 0 hingga batas ukuran memori.<br>
Baris 65: Mencetak nomor urut slot memori yang sedang diperiksa tanpa berpindah baris.<br>
Baris 66: Menunjuk variabel current ke isi data pertama pada nomor slot tersebut.<br>
Baris 67: Memeriksa apakah slot memori tersebut kosong tidak ada isinya sama sekali.<br>
Baris 68: Mencetak teks tulisan kosong jika slot memori tersebut bernilai None.<br>
Baris 69: (Baris Kosong)<br>
Baris 70: Memulai perulangan menyusuri rantai data jika slot tersebut berisi data kontak.<br>
Baris 71: Mencetak nama kontak beserta nomor teleponnya yang tersimpan di dalam simpul.<br>
Baris 72: Memeriksa apakah masih ada simpul data kontak lain di belakang simpul saat ini.<br>
Baris 73: Mencetak tanda panah tabrakan data (collision) jika ada kontak lain di belakangnya.<br>
Baris 74: Menggeser penunjuk current ke simpul berikutnya dalam rantai tersebut.<br>
Baris 75: Melakukan perpindahan baris baru setelah semua data di satu slot selesai dicetak.<br>
Baris 76: Mencetak garis pembatas bawah penutup visualisasi memori ke layar terminal.<br>
Baris 77: (Baris Kosong)<br>
Baris 78: Membuat fungsi main sebagai pengendali utama alur jalannya program.<br>
Baris 79: Membuat objek buku kontak baru dari class BukuKontakHashMap berkapasitas 5 slot.<br>
Baris 80: (Baris Kosong)<br>
Baris 81: Memulai perulangan tanpa batas agar aplikasi menu terus berjalan berulang-ulang.<br>
Baris 82: Mencetak judul menu aplikasi buku kontak ponsel ke layar terminal.<br>
Baris 83: Mencetak pilihan menu 1 untuk operasi tambah atau update nomor kontak baru.<br>
Baris 84: Mencetak pilihan menu 2 untuk operasi pencarian nomor telepon kontak.<br>
Baris 85: Mencetak pilihan menu 3 untuk operasi penghapusan data kontak dari ponsel.<br
Baris 86: Mencetak pilihan menu 4 untuk mengintip kondisi fisik slot penyimpanan memori.<br>
Baris 87: Mencetak pilihan menu 5 untuk menutup dan keluar dari aplikasi buku kontak.<br>
Baris 88: Mencetak garis pembatas bawah menu utama ke layar terminal.<br>
Baris 89: (Baris Kosong)<br>
Baris 90: Menangkap input angka pilihan menu dari ketikan keyboard pengguna.<br>
Baris 91: (Baris Kosong)<br>
Baris 92: Mengecek apakah pengguna memilih menu angka 1.<br>
Baris 93: Mencetak sub-judul operasi penambahan dan pembaruan data kontak ke layar.<br>
Baris 94: Menangkap input ketikan teks nama kontak dari pengguna lalu menghapus spasi kosong.<br>
Baris 95: Memeriksa apakah input nama kontak yang dimasukkan kosong tidak diisi.<br>
Baris 96: Menampilkan pesan kesalahan dan mengulang menu jika nama diisi kosong.<br
Baris 97: Menangkap input ketikan teks nomor telepon dari pengguna lalu menghapus spasi kosong.<br>
Baris 98: Memeriksa apakah input nomor telepon yang dimasukkan kosong tidak diisi.<br>
Baris 99: Menampilkan pesan kesalahan dan mengulang menu jika nomor diisi kosong.<br>
Baris 100: Memanggil fungsi insert untuk memproses dan menyimpan data kontak ke tabel hash.<br>
Baris 101: (Baris Kosong)<br>
Baris 102: Mengecek apakah pengguna memilih menu angka 2.<br>
Baris 103: Mencetak sub-judul operasi pencarian data kontak ke layar terminal.<br>
Baris 104: Menangkap input ketikan nama kontak yang ingin dicari nomor teleponnya.<br>
Baris 105: Memanggil fungsi search untuk melacak keberadaan data kontak di tabel hash.<br>
Baris 106: Memeriksa apakah data kontak yang dicari berhasil ditemukan (tidak None).<br>
Baris 107: Menampilkan informasi detail nama dan nomor telepon yang ditemukan ke layar.<br>
Baris 108: (Baris Kosong)<br>
Baris 109: Menampilkan informasi bahwa nama kontak tidak terdaftar jika hasil pencarian kosong.<br>
Baris 110: (Baris Kosong)<br>
Baris 111: Mengecek apakah pengguna memilih menu angka 3.<br>
Baris 112: Mencetak sub-judul operasi penghapusan data kontak ke layar terminal.<br>
Baris 113: Menangkap input ketikan nama kontak yang ingin dihapus dari memori ponsel.<br>
Baris 114: Memanggil fungsi remove_key untuk memproses pemutusan rantai kontak di tabel hash.<br>
Baris 115: (Baris Kosong)<br>
Baris 116: Mengecek apakah pengguna memilih menu angka 4.<br>
Baris 117: Memanggil fungsi display untuk memunculkan struktur peta slot memori di terminal.<br>
Baris 118: (Baris Kosong)<br>
Baris 119: Mengecek apakah pengguna memilih menu angka 5.<br>
Baris 120: Mencetak ucapan terima kasih dan salam perpisahan penutupan aplikasi ke layar.<br>
Baris 121: Menghentikan paksa perulangan menu utama agar program selesai berjalan.<br>
Baris 122: (Baris Kosong)<br>
Baris 123: Menangani kondisi jika pengguna menginputkan karakter di luar angka menu 1 sampai 5.<br>
Baris 124: Menampilkan notifikasi pesan kesalahan bahwa input menu pengguna tidak valid.<br>
Baris 125: (Baris Kosong)<br>
Baris 126: Menahan tampilan layar sementara agar pengguna sempat membaca output di layar.<br>
Baris 127: Membersihkan layar terminal agar kembali bersih sebelum menampilkan menu utama lagi.<br>
Baris 128: (Baris Kosong)<br>
Baris 129: Mengecek apakah file skrip Python ini dijalankan sebagai program utama.<br>
Baris 130: Memanggil fungsi main() untuk memicu jalannya seluruh rangkaian program aplikasi.<br>
<br>
outputnya:<br>
<img width="1651" height="864" alt="Screenshot 2026-06-09 194452" src="https://github.com/user-attachments/assets/8f4ef5d8-a1fc-4b49-9456-1e55070fa37c" />
<img width="1648" height="566" alt="Screenshot 2026-06-09 194706" src="https://github.com/user-attachments/assets/aaa9fe1e-5b14-466e-a749-53a8cfd3c196" />
pejelasan outputnya:<br>
Proses Tambah Data: Pengguna berhasil menginputkan data kontak baru secara manual, yaitu Nama: wawan dan Nomor Telepon/HP: 081234567. Setelah menekan Enter, sistem memberikan respons balik [SUKSES] Kontak 'wawan' berhasil disimpan., menandakan bahwa data telah sukses dipetakan oleh fungsi hash dan masuk ke dalam memori.<br>
<br>
Perulangan Menu: Sistem membersihkan layar dan kembali menampilkan 5 daftar menu utama secara rapi, siap untuk menerima instruksi interaksi berikutnya dari pengguna.<br>
<br>
Alokasi Slot Memori: Tabel memiliki 5 ruang penyimpanan (Slot 0 sampai Slot 4). Slot 0, Slot 1, dan Slot 4 saat ini berstatus kosong (KOSONG (EMPTY)).<br>
<br>
Penyimpanan Data Tunggal: Pada Slot 3, terdapat satu data kontak tunggal yang disimpan, yaitu (budi -> 08123).<br>
<br>
Fenomena Tabrakan Data (Collision): Pada Slot 2, terjadi kondisi di mana nama kontak siti dan wawan menghasilkan nilai indeks hash yang sama. Sistem berhasil menangani benturan ini tanpa menimpa data lama dengan cara merangkaikannya menggunakan rantai Linked List, yang divisualisasikan dengan tanda penunjuk arah ==collision==>.<br>
Link Youtube:<br>
