class Node:
    def __init__(self, key, value):
        self.key = key       
        self.value = value   
        self.next = None

class BukuKontakHashMap:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (hash(key) % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.value = value
                print(f"✓ Kontak '{key}' berhasil diperbarui.")
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        print(f"✓ Kontak '{key}' berhasil ditambahkan.")

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                print(f"✓ Kontak '{key}' berhasil dihapus.")
                return True
            prev = current
            current = current.next
            
        print(f"✗ Kontak '{key}' tidak ditemukan.")
        return False

    def display(self):
        print("\n=== Penyimpanan Internal Hash Table ===")
        for i in range(self.SIZE):
            print(f"Slot {i}: ", end="")
            current = self.table[i]
            if current is None:
                print("EMPTY")
            else:
                while current is not None:
                    print(f"[{current.key} : {current.value}] -> ", end="")
                    current = current.next
                print("None")

def main():
    buku_kontak = BukuKontakHashMap(size=5)

    print("Memasukkan data kontak awal...")
    buku_kontak.insert("Budi", "081234567890")
    buku_kontak.insert("Andi", "085711223344")
    buku_kontak.insert("Siti", "089988776655")
    
    while True:
        print("\n===== APLIKASI BUKU KONTAK PONSEL =====")
        print("1. Tambah / Update Kontak")
        print("2. Cari Nomor Telepon")
        print("3. Hapus Kontak")
        print("4. Tampilkan Memori Hash Table")
        print("5. Keluar")
        try:
            pilihan = int(input("Pilih menu (1-5): "))
        except ValueError:
            print("✗ Masukkan input berupa angka!")
            continue
            
        if pilihan == 1:
            nama = input("Masukkan Nama Kontak : ")
            no_telp = input("Masukkan Nomor Telp : ")
            buku_kontak.insert(nama, no_telp)
        elif pilihan == 2:
            nama = input("Cari Nama Kontak : ")
            hasil = buku_kontak.search(nama)
            if hasil is not None:
                print(f"➔ Kontak Ditemukan! {hasil.key} : {hasil.value}")
            else:
                print(f"✗ Kontak dengan nama '{nama}' tidak ditemukan.")
        elif pilihan == 3:
            nama = input("Masukkan nama kontak yang akan dihapus: ")
            buku_kontak.remove_key(nama)
        elif pilihan == 4:
            buku_kontak.display()
        elif pilihan == 5:
            print("Keluar dari aplikasi buku kontak. Terima kasih!")
            break
        else:
            print("✗ Pilihan menu tidak valid!")

if __name__ == "__main__":
    main()
