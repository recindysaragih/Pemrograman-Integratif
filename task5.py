total_sum = 0
angka = 0

print("Masukkan angka satu per satu (masukkan -1 untuk selesai):")

while angka != -1:
        angka = float(input())
        
        if angka != -1:
            total_sum += angka

print("Jumlah dari semua angka yang dimasukkan adalah:", total_sum)
