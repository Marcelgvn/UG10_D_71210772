# Marcellino Giovani Handoko Suwigjo Putro
# UG 10
# Variable 

A = int(input("Nilai A : "))
B = int(input("Nilai B : "))
C = int(input("Nilai C : "))

D = B**2 - 4 * A * C
X1 = (  -B + D / 2 ) / 2 * A
X2 = (  -B - D / 2 ) / 2 * A

if D < 0 :
    print("Fungsi tersebut tidak memiliki akar rill")

elif D > 0 :
    print("Akar-akar dari persamaan tersebut adalah ",X2,"dan",X1)

elif D == 0 :
    print("Fungsi tersebut memiliki akar kembar yaitu",X1)
    