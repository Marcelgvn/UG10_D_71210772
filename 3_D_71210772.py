# Marcellino Giovani Handoko Suwigjo Putro
# UG 10
# Variable 

Daftar1 = input("Masukkan daftar belanja Anda : ")
List1 = Daftar1.title()
List2 = List1.split(", ")

print("Daftar belanja : ", List2)
Daftar2 = (input("Masukkan barang yang ingin ditambahkan : "))

if (Daftar2.title() in List2) == True: 
	print("Barang", Daftar2.upper(), "sudah berada dalam daftar belanja.")

else: 
	#tambahbarang = List2 += _Daftar2

	_Daftar2 = Daftar2.upper()
	List2.append(_Daftar2)
	print("Hasil penambahan pada daftar belanja : ", List2)

