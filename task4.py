angka = int(input("Masukkan suatu angka: "))
deret_hasil= '+'.join(map(str, range(1, angka + 1)))
hasil_penjumlahan = sum(range(1, angka + 1))

print("Hasil" , hasil_penjumlahan)
print(deret_hasil)
