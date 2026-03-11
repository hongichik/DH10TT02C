a = float(input("Nhap canh a:"))
b = float(input("Nhap canh b:"))
c = float(input("Nhap canh c:"))

if a <= 0 or b <=0 or c <= 0:
    print("Khong phai tam giac")
else:
    if a +b <= c or a + c <= b or b + c <= a:
        print("Khong phai tam giac")
    else:
        if a == b and b == c:
            print("Tam giac deu")
        elif a == b or a == c or b == c:
            print("Tam giac can")
        else:
            if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
                print("Tam giac vuong")
            else:
                print("Tam giac thuong")