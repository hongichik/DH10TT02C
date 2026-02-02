a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

# Kiem tra tam giac hop le
if a + b <= c or a + c <= b or b + c <= a:
    print("Khong phai tam giac")
else:
    if a == b == c:
        print("Tam giac deu")
    elif a == b or a == c or b == c:
        print("Tam giac can")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Tam giac vuong")
    else:
        print("Tam giac thuong")