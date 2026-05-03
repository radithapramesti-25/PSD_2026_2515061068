# Program Merapikan Uang Kertas di Kasir
def insertion_sort_uang(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
    
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def main():
    print("=== PROGRAM KASIR: MERAPIKAN UANG KERTAS ===")
    try:
        n = int(input("Masukkan jumlah lembar uang: "))
    except ValueError:
        print("Input tidak valid! Masukkan angka.")
        return

    uang_kertas = []
    print("\nMasukkan nominal setiap lembar uang (contoh: 5000):")
    for i in range(n):
        while True:
            try:
                nominal = int(input(f"Lembar ke-{i+1}: "))
                uang_kertas.append(nominal)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka nominal!")

    print(f"\nKondisi uang berantakan: {uang_kertas}")

    # Memanggil fungsi sorting
    insertion_sort_uang(uang_kertas, n)

    print("\nProses merapikan selesai...")
    print("Uang kertas yang sudah rapi (Terkecil -> Terbesar):")
    for i in range(n):
        print(f"Rp{uang_kertas[i]}", end=" ")
    print("\n")

if __name__ == "__main__":
    main()
