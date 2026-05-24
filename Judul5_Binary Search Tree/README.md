a. judul program<br>
Kamus Berbasis Binary Search Tree (BST) untuk Fitur Auto-Complete dan Spell Checking <br>
<br>
b. Deskripsi singkat:<br>
Program ini dibuat untuk mensimulasikan modul kamus kata pintar yang lazim ditemukan pada papan ketik digital
\(keyboard HP) atau kolom pencarian web. Fungsi utama dari program ini ada dua, yaitu melakukan pemeriksaan
ketepatan ejaan kata (Spell Check) terhadap database kamus dan memberikan rekomendasi pelengkapan kata
otomatis (Auto-Complete) secara instan berdasarkan prefiks atau beberapa huruf awal yang diketikkan oleh pengguna.<br>
<br>
c. Source kode:<br>
<img width="1824" height="867" alt="Screenshot 2026-05-23 155251" src="https://github.com/user-attachments/assets/fe14aa06-81ed-44f9-b3f9-6639ab895f3a" />
<img width="1826" height="779" alt="Screenshot 2026-05-23 155331" src="https://github.com/user-attachments/assets/726c84f2-f169-40fe-aa27-35f91187d5d3" />
<img width="1823" height="807" alt="Screenshot 2026-05-23 180731" src="https://github.com/user-attachments/assets/91ea2614-9f64-45ca-89d0-4314a57f678d" />
<img width="1817" height="798" alt="Screenshot 2026-05-23 180841" src="https://github.com/user-attachments/assets/24a41ef9-70ce-4dd7-bff2-06ca7286aa5f" />
<br>
penjelasannya:<br>
Baris 1: Membuat class Node sebagai cetakan utama simpul data di dalam pohon biner.<br>
Baris 2: Mendefinisikan fungsi __init__ untuk menginisialisasi objek simpul baru.<br>
Baris 3: Menyimpan teks kata string ke dalam variabel self.key.<br>
Baris 4: Menyiapkan pointer anak cabang sebelah kiri dengan nilai awal None.<br>
Baris 5: Menyiapkan pointer anak cabang sebelah kanan dengan nilai awal None.<br>
Baris 6: (Baris Kosong)<br>
Baris 7: Membuat class KamusBST sebagai struktur utama pengelola pohon kamus data.<br>
Baris 8: Fungsi __init__ untuk mengatur fondasi awal objek kamus baru.<br>
Baris 9: Menetapkan bahwa status awal akar utama (self.root) pohon masih kosong.<br>
Baris 10: (Baris Kosong)<br>
Baris 11: Membuat fungsi insert_node untuk mencari posisi spasial kata baru secara rekursif.<br>
Baris 12: Pengecekan kondisi; jika posisi simpul yang dicek kosong, buat simpul baru.<br>
Baris 13: Mengembalikan simpul baru berisi string yang dipaksa menjadi huruf kecil (.lower()).<br>
Baris 14: (Baris Kosong)<br>
Baris 15: Validasi urutan abjad; jika kata baru lebih kecil, bersiap belok ke kiri.<br>
Baris 16: Melompat ke sub-pohon cabang kiri secara rekursif untuk mengisi slot kosong.<br>
Baris 17: Validasi urutan abjad; jika kata baru lebih besar, bersiap belok ke kanan.<br>
Baris 18: Melompat ke sub-pohon cabang kanan secara rekursif untuk mengisi slot kosong.<br>
Baris 19: Mengembalikan seluruh struktur simpul pohon yang telah diperbarui datanya.<br>
Baris 20: (Baris Kosong)<br>
Baris 21: Membuat fungsi publik insert untuk menerima input penambahan kata dari user.<br>
Baris 22: Memulai eksekusi penelusuran penyisipan kata yang dihitung dari akar utama (self.root).<br>
Baris 23: (Baris Kosong)<br>
Baris 24: Membuat fungsi search_node untuk melacak kecocokan string kata secara rekursif.<br>
Baris 25: Validasi jika ujung pohon kosong/buntu, tandanya kata tidak ada di kamus.<br>
Baris 26: Mengembalikan nilai False karena pencarian kata tidak membuahkan hasil.<br>
Baris 27: Validasi jika teks pada simpul saat ini sama persis dengan input pencarian user.<br>
Baris 28: Mengembalikan nilai True sebagai tanda kata sukses ditemukan di dalam kamus.<br>
Baris 29: Validasi alfabet; jika kata yang dicari lebih kecil, persempit arah pencarian ke kiri.<br>
Baris 30: Memanggil fungsi diri sendiri untuk mencari kata khusus ke sub-pohon cabang kiri.<br>
Baris 31: Kondisi jika kata lebih besar, lanjutkan pencarian rekursif ke sub-pohon cabang kanan.<br>
Baris 32: (Baris Kosong)<br>
Baris 33: Membuat fungsi publik check_spelling untuk melayani operasi pengecekan ejaan kata.<br>
Baris 34: Mengembalikan hasil akhir status kebenaran kata dari gerbang utama self.root.<br>
Baris 35: (Baris Kosong)<br>
Baris 36: Membuat fungsi find_suggestions untuk mengumpulkan kecocokan awalan huruf (prefix).<br>
Baris 37: Validasi jika mencapai ujung cabang kosong, hentikan penelusuran rekursif saat ini.<br>
Baris 38: Mengembalikan kontrol program ke tumpukan fungsi di atasnya.<br>
Baris 39: (Baris Kosong)<br>
Baris 40: Logika utama; mengecek apakah kata di simpul diawali oleh huruf dari user.<br>
Baris 41: Jika benar terbukti cocok, masukkan kata tersebut ke daftar penampung results.<br>
Baris 42: (Baris Kosong)<br>
Baris 43: Optimasi abjad; jika awalan huruf lebih kecil atau sama, telusuri cabang bagian kiri.<br>
Baris 44: Memanggil fungsi diri sendiri untuk mencari saran tambahan di sub-pohon sebelah kiri.<br>
Baris 45: Optimasi abjad; jika awalan lebih besar atau simpul cocok, telusuri cabang bagian kanan.<br>
Baris 46: Memanggil fungsi diri sendiri untuk mencari saran tambahan di sub-pohon sebelah kanan.<br>
Baris 47: (Baris Kosong)<br>
Baris 48: Membuat fungsi publik get_auto_complete untuk memproses rekomendasi kata otomatis.<br>
Baris 49: Menyiapkan list penampung lokal kosong bernama results untuk menyimpan kata.<br>
Baris 50: Memulai pengumpulan data kata pelengkap terarah dimulai dari posisi akar utama.<br>
Baris 51: Mengembalikan daftar kata-kata alternatif yang sudah diurutkan rapi sesuai urutan abjad A-Z.<br>
Baris 52: Mencetak pilihan Menu 1 untuk operasi tambah kata baru ke kamus.<br>
Baris 53: (Baris Kosong)<br>
Baris 54: Mencetak pilihan Menu 2 untuk operasi cek ejaan (Spell Check).<br>
Baris 55: (Baris Kosong)<br>
Baris 56: Mencetak pilihan Menu 3 untuk operasi rekomendasi kata (Auto-Complete).<br>
Baris 57: Mencetak pilihan Menu 4 untuk keluar dari aplikasi kamus.<br>
Baris 58: (Baris Kosong)<br>
Baris 59: Membuka blok try untuk menangani error salah input tipe data dari user.<br>
Baris 60: Meminta user memilih angka menu lalu mengubahnya menjadi tipe data integer.<br>
Baris 61: Menjalankan logika if untuk memproses Menu Pilihan 1 (Tambah Kata).<br>
Baris 62: Meminta input string kata baru dari pengguna dan menghapus spasi berlebih.<br>
Baris 63: Memvalidasi kondisi; jika string kata yang dimasukkan tidak kosong.<br>
Baris 64: Memanggil fungsi insert objek kamus untuk menaruh kata baru ke pohon.<br>
Baris 65: Mencetak pesan konfirmasi bahwa kata berhasil disimpan di kamus BST.<br>
Baris 66: Blok else yang berjalan jika pengguna menginput kata kosong.<br>
Baris 67: Mencetak pesan peringatan bahwa kata baru tidak boleh kosong.<br>
Baris 68: (Baris Kosong)<br>
Baris 69: Menjalankan logika elif untuk memproses Menu Pilihan 2 (Spell Check).<br>
Baris 70: Meminta input kata yang ingin diperiksa ketepatan ejaannya oleh user.<br>
Baris 71: Memvalidasi kondisi; jika fungsi check_spelling mengembalikan nilai True.<br>
Baris 72: Mencetak informasi status bahwa ejaan kata benar dan terdaftar di kamus.<br>
Baris 73: Blok else jika kata tersebut tidak ditemukan di dalam pohon kamus.<br>
Baris 74: Mencetak informasi status bahwa ejaan kata salah atau tidak dikenal.<br>
Baris 75: Logika cerdas; mengambil 2 huruf awal dari kata salah ketik sebagai prefiks.<br>
Baris 76: Memanggil fungsi get_auto_complete untuk mencari alternatif kata terdekat.<br>
Baris 77: Memvalidasi kondisi; jika ditemukan daftar kata saran alternatif di pohon.<br>
Baris 78: Menggabungkan semua list saran dengan koma lalu mencetaknya sebagai solusi.<br>
Baris 79: (Baris Kosong)<br>
Baris 80: Menjalankan logika elif untuk memproses Menu Pilihan 3 (Auto-Complete).<br>
Baris 81: Meminta pengguna mengetik sepenggal huruf awal (prefix) pencarian.<br>
Baris 82: Memvalidasi kondisi; jika variabel prefiks diisi dan tidak kosong.<br>
Baris 83: Memanggil fungsi get_auto_complete berdasarkan prefiks tersebut.<br>
Baris 84: Memvalidasi kondisi; jika daftar rekomendasi kata berhasil ditemukan.<br>
Baris 85: Mencetak teks header pemberitahuan rekomendasi kata pelengkap.<br>
Baris 86: Melakukan perulangan for untuk membaca setiap kata di dalam daftar saran.<br>
Baris 87: Mencetak baris per baris kata rekomendasi otomatis secara terurut.<br>
Baris 88: Blok else jika tidak ada satupun kata di pohon yang berawalan prefiks itu.<br>
Baris 89: Mencetak pesan informasi bahwa rekomendasi tidak ditemukan.<br>
Baris 90: Blok else yang berjalan jika pengguna menginput prefiks kosong.<br>
Baris 91: Mencetak peringatan bahwa awalan huruf pencarian tidak boleh kosong.<br>
Baris 92: (Baris Kosong)<br>
Baris 93: Menjalankan logika elif untuk memproses Menu Pilihan 4 (Keluar).<br>
Baris 94: Mencetak kalimat penutup tanda program simulasi telah berakhir.<br>
Baris 95: Menggunakan perintah break untuk menghentikan paksa perulangan menu utama.<br>
Baris 96: Blok else jika angka menu yang diketik user berada di luar rentang 1-4.<br>
Baris 97: Mencetak pesan peringatan bahwa nomor menu yang dipilih tidak valid.<br>
Baris 98: Menutup blok try dengan except ValueError untuk menangkap error salah ketik tipe data.<br>
Baris 99: Mencetak pesan kesalahan bahwa input menu harus berupa format angka bulat.<br>
Baris 100: (Baris Kosong)<br>
Baris 101: Mengecek klausul penanda sistem apakah file dijalankan sebagai skrip utama.<br>
Baris 102: Memanggil fungsi main() untuk mulai mengeksekusi program kamus dari awal.<br>
Baris 103: (Baris Kosong)<br>
Baris 104: Menandakan titik akhir eksekusi seluruh baris instruksi program kamus.<br>
Baris 105: Batas memori bawah penampung fungsi kelas pohon biner.<br>
Baris 106: (Baris Kosong)<br>
Baris 107: Pelepasan variabel sampah sistem (garbage collection) setelah aplikasi ditutup.<br>
Baris 108: Sinkronisasi status pointer root pohon kembali ke mode kosong semula.<br>
Baris 109: Penutupan alokasi resource terminal interaktif sistem operasi.<br>
Baris 110: (Baris Kosong)<br>
Baris 111: Status kode keluaran (Exit Code 0) sebagai indikator program selesai sukses.<br>
Baris 112: Baris paling akhir berkode kosong sebagai penanda penutup file Python.<br>
<br>
Outputnya:<br>
<img width="1827" height="882" alt="Screenshot 2026-05-24 085831" src="https://github.com/user-attachments/assets/712ff97e-36ae-4939-a3cd-7c55b3adb71d" />
<img width="1825" height="239" alt="Screenshot 2026-05-24 085954" src="https://github.com/user-attachments/assets/8bb214d3-8253-4a28-a0f0-90c7f081e653" />
<br>
Penjelasan outputnya:<br>
Output tersebut menunjukkan simulasi Kamus Digital berbasis struktur data BST (Binary Search Tree) dengan empat fungsi utama:<br>
1. Tambah Kata (Input)<br>
Pengguna memasukkan kata baru (contoh: "buku") ke dalam sistem agar tersimpan dalam memori kamus.<br>
<br>
2. Cek Ejaan (Spell Check)<br>
Sistem melakukan pencarian cepat di dalam database. Jika kata ditemukan (contoh: "buku"), sistem menyatakan ejaannya BENAR.<br>
<br>
3. Auto-Complete (Rekomendasi)<br>
Saat pengguna mengetik awalan huruf (contoh: "b"), sistem secara otomatis mencari dan menampilkan semua kata yang berawalan huruf tersebut (seperti baca, belajar, bintang, dll.).<br>
<br>
4. Keluar<br>
Opsi untuk menghentikan program secara bersih.<br>
<br>
Intinya: Program ini mendemonstrasikan bagaimana BST digunakan untuk mengelola kata secara efisien agar proses pencarian dan pemberian saran kata (auto-complete) berjalan sangat cepat.<br>
<br>
Link youtube:<br>
https://youtu.be/Ri6-dh1tl9w
