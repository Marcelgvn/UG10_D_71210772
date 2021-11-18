# Marcellino Giovani Handoko Suwigjo Putro
# UG 10
# Variable 

A = int(input("Masukkan harga makanan sebesar Rp "))
B = int(input("Masukkan harga snack sebesar Rp "))
C = int(input("Masukkan harga minuman sebesar Rp " ))
D = int(input("Masukkan harga yang anda bawa Rp "))

Total_Harga = A + B + C
print("\nTotal yang harus anda bayar sebesar Rp ", Total_Harga)

if Total_Harga > D:
    print("Uang anda kurang! Anda memiliki utang sebesar Rp ", Total_Harga-D)
    
elif Total_Harga == D:
    print("Uang anda pas! Tidak ada kembalian dan utang :D")

else:
    print("Anda memiliki kembalian sebesar Rp", D-Total_Harga)

