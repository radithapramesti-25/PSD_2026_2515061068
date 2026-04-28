class Node:
    def __init__(self, judul, penyanyi):
        self.judul = judul
        self.penyanyi = penyanyi
        self.next = None

class PlaylistLagu:
    def __init__(self):
        self.start = None

    def tambah_lagu(self, judul, penyanyi):
        new_node = Node(judul, penyanyi)
        if self.start is None:
            self.start = new_node
        else:
            current = self.start
            while current.next is not None:
                current = current.next
            current.next = new_node
        print(f"\n[Sistem] Berhasil menambahkan: {judul} - {penyanyi}")

    def tampilkan_playlist(self):
        if self.start is None:
            print("\n[Info] Playlist masih kosong.")
            return
        
        print("\n========== DAFTAR PUTAR ANDA ==========")
        current = self.start
        no = 1
        while current is not None:
            print(f"{no}. {current.judul} ({current.penyanyi})")
            current = current.next
            no += 1
        print("=======================================")

def main():
    my_playlist = PlaylistLagu()
    
    print("Selamat Datang di Pembuat Playlist Linked List!")
    
    while True:
        print("\nMenu:")
        print("1. Tambah Lagu Baru")
        print("2. Lihat Playlist")
        print("3. Keluar")
        
        pilihan = input("Pilih menu (1/2/3): ")
        
        if pilihan == '1':
            judul = input("Masukkan Judul Lagu: ")
            penyanyi = input("Masukkan Nama Penyanyi: ")
            my_playlist.tambah_lagu(judul, penyanyi)
        
        elif pilihan == '2':
            my_playlist.tampilkan_playlist()
            
        elif pilihan == '3':
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()