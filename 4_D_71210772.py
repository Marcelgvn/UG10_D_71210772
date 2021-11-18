# Marcellino Giovani Handoko Suwigjo Putro
# UG 10
# Variable 

A = int(input("Masukan bilangan 1 : "))
B = int(input("Masukan bilangan 2 : "))
C = int(input("Masukan bilangan 3 : "))

if A >= B and A >= C and B >= C :
    print("Urutan bilangan dari yang terbesar adalah", A, B, C)
elif B >= A and B >= C and C >= A :
    print("Urutan bilangan dari yang terbesar adalah", B, C, A)

elif B >= A and B >= C and C >= A :
    print("Urutan bilangan dari yang terbesar adalah", B, A, C)

elif C >= A and C >= B and B >= A :
    print("Urutan bilangan dari yang terbesar adalah", C, B, A)

