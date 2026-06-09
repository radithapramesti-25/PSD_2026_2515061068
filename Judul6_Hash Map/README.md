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
Baris 1: Membuat class Node sebagai cetakan objek simpul untuk penanganan tabrakan data (Separate Chaining).<br>
Baris 2: Mendefinisikan fungsi __init__ untuk menginisialisasi atribut awal setiap objek simpul baru.<br>
Baris 3: Menyimpan parameter nama kontak ke dalam variabel instansi self.key.<br>
Baris 4: Menyimpan parameter nomor telepon ke dalam variabel instansi self.value.<br>
Baris 5: Mengatur pointer self.next dengan nilai default None sebagai penunjuk ke node selanjutnya.<br>
Baris 6: (Baris Kosong)<br>
Baris 7: Membuat class BukuKontakHashMap sebagai blueprint struktur utama tabel hash.<br>
Baris 8: Mendefinisikan fungsi __init__ untuk memesan kapasitas ruang penyimpanan tabel.<br>
Baris 9: Menyimpan batas ukuran maksimal tabel ke dalam variabel self.SIZE (default bernilai 10).<br>
Baris 10: Mengalokasikan array self.table berisi slot kosong (None) sebanyak jumlah kapasitas.<br>
Baris 11: (Baris Kosong)<br>
Baris 12: Membuat fungsi hash_function untuk mengonversi string nama kontak menjadi nilai indeks angka.<br>
Baris 13: Mengubah string nama menjadi integer, melakukan operasi modulo, dan mengembalikan indeks valid (0 sampai SIZE-1).<br>
Baris 14: (Baris Kosong)<br>
Baris 15: Membuat fungsi insert untuk menambahkan data kontak baru atau memperbarui data yang sudah ada.<br>
Baris 16: Memanggil fungsi hash_function untuk mencari letak nomor indeks slot dari nama kontak terkait.<br>
Baris 17: Mengarahkan variabel penunjuk current ke elemen pertama (head) pada slot tabel hasil hash.<br>
Baris 18: (Baris Kosong)<br>
Baris 19: Memulai perulangan untuk menelusuri rantai simpul linked list selama current tidak bernilai None.<br>
Baris 20: Mengecek apakah nama kontak (current.key) sudah sama persis dengan kunci yang dimasukkan.<br>
Baris 21: Menimpa nomor telepon lama dengan nomor telepon yang baru jika nama kontak sudah terdaftar.<br>
Baris 22: Mencetak pesan konfirmasi ke layar terminal bahwa data nomor telepon berhasil diperbarui.<br>
Baris 23: Menghentikan eksekusi fungsi insert menggunakan perintah return karena data telah diperbarui.<br>
Baris 24: Menggeser variabel penunjuk current maju ke simpul berikutnya di dalam untaian linked list.<br>
Baris 25: (Baris Kosong)<br>
Baris 26: Membuat objek simpul (Node) baru untuk menampung pasangan nama dan nomor telepon baru.<br>
Baris 27: Menghubungkan pointer next simpul baru ke alamat data yang sebelumnya menempati posisi terdepan slot.<br>
Baris 28: Menempatkan simpul baru tersebut menjadi elemen terdepan (head) di dalam slot indeks tabel hash.<br>
Baris 29: Mencetak pesan konfirmasi ke layar terminal bahwa kontak baru sukses ditambahkan.<br>
Baris 30: (Baris Kosong)<br>
Baris 31: Membuat fungsi search untuk mendeteksi dan mengambil data kontak berdasarkan nama.<br>
Baris 32: Mendapatkan nomor indeks slot penyimpanan berdasarkan nama kontak melalui fungsi hash.<br>
Baris 33: Mengarahkan variabel penunjuk current ke elemen terdepan pada slot tabel di indeks tersebut.<br>
Baris 34: (Baris Kosong)<br>
Baris 35: Memulai perulangan untuk mencari kecocokan nama kontak di sepanjang rantai linked list.<br>
Baris 36: Memeriksa apakah nama kontak pada simpul saat ini sama dengan nama kontak yang dicari.<br>
Baris 37: Mengembalikan seluruh objek simpul data kontak (current) jika target berhasil ditemukan.<br>
Baris 38: Menggeser variabel penunjuk current maju satu langkah ke simpul di belakangnya.<br>
Baris 39: Mengembalikan nilai None sebagai tanda bahwa nama kontak tidak ditemukan setelah penelusuran selesai.<br>
Baris 40: (Baris Kosong)<br>
Baris 41: Membuat fungsi remove_key untuk menghapus data kontak dari tabel hash berdasarkan nama.<br>
Baris 42: Mendapatkan nomor indeks slot penyimpanan dari nama kontak yang ingin dihapus via fungsi hash.<br>
Baris 43: Mengarahkan variabel penunjuk current ke elemen terdepan pada slot memori target.<br>
Baris 44: Membuat variabel bantu prev dengan nilai awal None untuk mencatat simpul sebelum current.<br>
Baris 45: (Baris Kosong)<br>
Baris 46: Memulai perulangan penyusuran linked list untuk memburu simpul kontak yang akan dihapus.<br>
Baris 47: Memeriksa apakah nama kontak pada simpul saat ini cocok dengan nama target yang akan dihapus.<br>
Baris 48: Memeriksa kondisi apakah simpul yang dicocokkan berada di urutan paling depan slot memori.<br>
Baris 49: Memindahkan penunjuk utama tabel di indeks tersebut langsung ke simpul di belakangnya (current.next).<br>
Baris 50: Mengondisikan pemutusan jika data di tengah/belakang, dengan mengarahkan pointer next simpul sebelum target melompati simpul target.<br>
Baris 51: Menghubungkan pointer simpul sebelumnya (prev.next) langsung ke simpul setelah target (current.next).<br>
Baris 52: Mencetak pesan konfirmasi sukses ke layar terminal bahwa data kontak telah berhasil dihapus.<br>
Baris 53: Mengembalikan nilai Boolean True sebagai tanda operasi penghapusan berhasil dituntaskan.<br>
Baris 54: Menyimpan posisi simpul saat ini ke dalam variabel prev sebelum penunjuk bergeser.<br>
Baris 55: Menggeser variabel penunjuk current maju ke simpul berikutnya di dalam untaian linked list.<br>
Baris 56: (Baris Kosong)<br>
Baris 57: Mencetak notifikasi bertanda silang jika perulangan habis dan nama kontak tidak ada di memori.<br>
Baris 58: Mengembalikan nilai Boolean False sebagai indikasi bahwa operasi penghapusan data gagal.<br>
Baris 59: (Baris Kosong)<br>
Baris 60: Membuat fungsi display untuk memvisualisasikan kondisi susunan slot memori internal tabel hash.<br>
Baris 61: Mencetak baris judul penanda peta penyimpanan internal tabel hash ke layar terminal.<br>
Baris 62: Melakukan perulangan terukur dari indeks 0 hingga batas kapasitas maksimal ukuran tabel hash.<br>
Baris 63: Mencetak label nomor slot memori yang sedang diperiksa tanpa melakukan perpindahan baris baru.<br>
Baris 64: Mengarahkan penunjuk variabel current ke elemen hulu pada nomor slot urutan ke-i.<br>
Baris 65: Mengecek situasi jika slot memori tersebut kosong atau tidak menyimpan data objek sama sekali.<br>
Baris 66: Mencetak teks tulisan "EMPTY" untuk menginformasikan bahwa slot tersebut kosong tanpa penghuni.<br>
Baris 67: Mengondisikan blok alternatif jika slot memori terdeteksi menyimpan rangkaian simpul data.<br>
Baris 68: Memulai perulangan sekuensial untuk mengekstrak isi rantai kontak selama current tidak kosong.<br>
Baris 69: Mencetak nama kontak serta nomor telepon di dalam simpul dalam format pasangan terstruktur.<br>
Line 70: Menggeser penunjuk variabel current maju untuk membaca data simpul di barisan belakangnya.<br>
Baris 71: Mencetak teks string "None" sebagai penanda visual akhir dari ujung rantai linked list.<br>
Baris 72: (Baris Kosong)<br>
Baris 73: Membuat fungsi main sebagai fungsi pengatur utama alur skenario jalannya program.<br>
Baris 74: Menginstansiasi objek buku kontak baru dengan mengeset kapasitas ukuran tabel sebanyak 5 slot.<br>
Baris 75: (Baris Kosong)<br>
Baris 76: Mencetak teks pemberitahuan proses pengisian data muatan mula-mula ke layar.<br>
Baris 77: Memasukkan data kontak awal pertama dengan Nama: "Budi" dan Nomor: "081234567890".<br>
Baris 78: Memasukkan data kontak awal kedua dengan Nama: "Andi" dan Nomor: "085711223344".<br>
Baris 79: Memasukkan data kontak awal ketiga dengan Nama: "Siti" dan Nomor: "089988776655".<br>
Baris 80: (Baris Kosong)<br>
Baris 81: Membuka struktur kontrol blok perulangan while True untuk memproses menu interaktif tanpa henti.<br>
Baris 82: Mencetak baris teks komponen judul atas dari aplikasi buku kontak ponsel.<br>
Baris 83: Mencetak teks pilihan opsi menu ke-1 untuk melakukan penambahan atau pembaruan kontak.<br>
Baris 84: Mencetak teks pilihan opsi menu ke-2 untuk melakukan pencarian nomor telepon kontak.<br>
Baris 85: Mencetak teks pilihan opsi menu ke-3 untuk mengeksekusi penghapusan data kontak.<br>
Baris 86: Mencetak teks pilihan opsi menu ke-4 untuk menampilkan visual memori internal tabel hash.<br>
Baris 87: Mencetak teks pilihan opsi menu ke-5 untuk keluar dan menghentikan proses aplikasi.<br>
Baris 88: Membuka blok penanganan kesalahan try untuk mengantisipasi kesalahan ketik input dari pengguna.<br>
Baris 89: Mengambil data masukan dari keyboard pengguna dan mengonversinya langsung menjadi tipe integer.<br>
Baris 90: Menangkap galat ValueError jika pengguna tidak menginputkan karakter berbentuk nomor angka bulat.<br>
Baris 91: Memberikan umpan balik peringatan agar pengguna mengetikkan masukan berupa tipe angka saja.<br>
Baris 92: Memberikan instruksi continue untuk melompat kembali ke awal perulangan menu utama.<br>
Baris 93: (Baris Kosong)<br>
Baris 94: Melakukan pengujian logis jika angka pilihan menu yang dimasukkan pengguna adalah 1.<br>
Baris 95: Mengambil input ketikan teks keyboard dari pengguna untuk mengisi nama kontak baru.<br>
Baris 96: Mengambil input ketikan teks keyboard dari pengguna untuk mengisi nomor telepon kontak baru.<br>
Baris 97: Memanggil fungsi insert milik objek buku_kontak untuk menyimpan atau meng-update data.<br>
Baris 98: Melakukan pengujian logis jika angka pilihan menu yang dimasukkan pengguna adalah 2.<br>
Baris 99: Meminta pengguna mengetikkan nama kontak yang ingin dilacak nomor teleponnya.<br>
Baris 100: Memanggil fungsi search untuk melakukan pencarian dan hasilnya ditampung di variabel hasil.<br>
Baris 101: Memeriksa apakah variabel hasil sukses mendapatkan objek simpul kontak (tidak None).<br>
Baris 102: Menampilkan nama kontak beserta informasi nomor teleponnya secara lengkap ke layar.<br>
Baris 103: Mengondisikan blok alternatif jika pencarian nama kontak menghasilkan nilai kosong (None).<br>
Baris 104: Menampilkan pesan teks informasi bahwa nama kontak yang dicari tidak terdaftar.<br>
Baris 105: Melakukan pengujian logis jika angka pilihan menu yang dimasukkan pengguna adalah 3.<br>
Baris 106: Meminta pengguna memasukkan nama kontak yang ingin dihapus secara permanen dari ponsel.<br>
Baris 107: Memanggil fungsi remove_key untuk mengeksekusi penghapusan simpul dari struktur tabel hash.<br>
Baris 108: Melakukan pengujian logis jika angka pilihan menu yang dimasukkan pengguna adalah 4.<br>
Baris 109: Memanggil fungsi display untuk memunculkan kondisi visual internal slot memori tabel hash.<br>
Baris 110: Melakukan pengujian logis jika angka pilihan menu yang dimasukkan pengguna adalah 5.<br>
Baris 111: Mencetak teks kalimat salam perpisahan penutupan aplikasi ke layar terminal.<br>
Baris 112: Menggunakan perintah break untuk keluar dari loop while guna mematikan jalannya skrip.<br>
Baris 113: Mengondisikan penanganan jika angka menu yang diketik berada di luar jangkauan angka 1-5.<br>
Baris 114: Mencetak pesan teks peringatan bahwa pilihan menu yang dimasukkan tidak valid.<br>
Baris 115: (Baris Kosong)<br>
Baris 116: Mengecek kondisi lingkungan apakah file ini bertindak sebagai modul utama yang dijalankan.<br>
Baris 117: Mengeksekusi fungsi main() untuk mengaktifkan seluruh fungsionalitas program dari awal.<br>
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
