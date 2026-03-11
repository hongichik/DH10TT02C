n = int(input("Nhap so n: "))

if n <= 1:
    print("Khong phai so nguyen to")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Khong phai so nguyen to")
            break
    else:
        print("La so nguyen to")
