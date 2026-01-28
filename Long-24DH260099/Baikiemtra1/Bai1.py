try:
    a = float(input("Nhap canh a: "))
    b = float(input("Nhap canh b: "))
    c = float(input("Nhap canh c: "))
    if (a + b > c) and (a + c > b) and (b + c > a):
        if a == b == c:
            print("Day la tam giac deu")
        elif (a == b) or (a == c) or (b == c):
            print("Day la tam giac can")
        elif (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
            print("Day la tam giac vuong")
        else:
            print("Day la tam giac thuong")
    else:
        print("Khong phai tam giac")
except ValueError:
    print("Vui long chi nhap so thuc hop le!")