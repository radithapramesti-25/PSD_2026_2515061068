class StackGudang:
    def __init__(self, kapasitas=100):
        self.MAX = kapasitas
        self.barang = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, nama_barang):
        if self.is_full():
            print(f"\n[!] Gagal: Gudang penuh! '{nama_barang}' tidak bisa masuk.")
        else:
            self.top_idx += 1
            self.barang[self.top_idx] = nama_barang
            print(f"\n[+] Berhasil: '{nama_barang}' disimpan di tumpukan teratas.")

    def pop(self):
        if self.is_empty():
            print("\n[!] Gagal: Gudang kosong, tidak ada barang yang bisa diambil.")
            return None
        else:
            barang_diambil = self.barang[self.top_idx]
            self.top_idx -= 1
            print(f"\n[-] Berhasil: '{barang_diambil}' telah dikeluarkan.")
            return barang_diambil

    def peek(self):
        if self.is_empty():
            print("\n[i] Status: Gudang kosong.")
        else:
            print(f"\n[i] Barang teratas saat ini: {self.barang[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("\nStatus: Gudang Kosong.")
        else:
            print("\n========== ISI GUDANG NILA ==========")
            for i in range(self.top_idx, -1, -1):
                print(f"| [{i}] {self.barang[i]} |")
            print("=======================================")

def main():
    print("Selamat Datang di Sistem Logistik Gudang NILA Otomatis")
    try:
        kapasitas = int(input("Tentukan kapasitas maksimal lorong gudang: "))
    except ValueError:
        kapasitas = 5
        print("Input tidak valid, kapasitas diset ke default (5).")

    gudang = StackGudang(kapasitas)

    while True:
        print("\nMenu Operasi:")
        print("1. Push (Masukan Barang)")
        print("2. Pop (Ambil Barang Teratas)")
        print("3. Peek (Cek Barang Teratas)")
        print("4. Display (Lihat Semua Barang)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            nama = input("Masukkan nama barang: ")
            gudang.push(nama)
        elif pilihan == '2':
            gudang.pop()
        elif pilihan == '3':
            gudang.peek()
        elif pilihan == '4':
            gudang.display()
        elif pilihan == '5':
            print("Terima kasih telah menggunakan sistem gudang.")
            break
        else:
            print("Pilihan tidak tersedia, silakan coba lagi.")

if __name__ == "__main__":
    main()
