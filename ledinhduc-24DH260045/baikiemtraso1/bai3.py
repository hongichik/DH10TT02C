import math
n = int(input("Nhap mot so nguyen duong n (n > 1): "))

if n <= 1:
    print("Vui long nhap so lon hon 1.")
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(f"{n} khong phai la so nguyen to")
            break
    else:
        print(f"{n} la so nguyen to")