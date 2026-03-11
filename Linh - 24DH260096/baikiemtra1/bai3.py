so = int(input("Nhap so nguyen duong n: "))

if so <=1:
    print("Khong phai so nguyen to")
else:
    for i in range(2, so):
        if so%i==0:
            print("Khong phai so nguyen to")
            break
    else:
        print("La so nguyen to")

