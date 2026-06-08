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
