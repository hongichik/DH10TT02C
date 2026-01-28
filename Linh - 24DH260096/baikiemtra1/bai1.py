a = int(input("Nhap canh a: "))
b = int(input("Nhap canh b: "))
c = int(input("Nhap canh c: "))
if a + b <= c or b + c <= a or a + c <= b:
    print("Khong phai tam giac")
else:
    if a == b == c:
        print("Tam giac deu")
    elif a == b or b == c or a == c:
        print("Tam giac can")
    elif a^2 + b^2 == c^2 or a^2 + c^2 == b^2 or b^2 + c^2 == a^2:
        print("Tam giac vuong")
    else:
        print("Tam giac thuong")

