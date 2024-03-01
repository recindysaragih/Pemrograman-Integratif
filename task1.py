import math

gaji_tahunan = float(input("Masukkan gaji tahunan Anda: "))
gaji_bulanan = math.ceil(gaji_tahunan / 12)

print("Gaji bulanan Anda adalah:", gaji_bulanan)