n = int(input("Nhap n (n > 1): "))
for i in range(2, n):
    if n % i == 0:
        print("Khong phai so nguyen to")
        break
else:
    print("La so nguyen to")
    #bai3