a = float(input("nhap canh a:"))
b = float(input("nhap canh b:"))
c = float(input("nhap canh c:"))
if a + b < c or b + c < a or a + c < b:
    print("khong phai tam giac")
else:
    if a == b == c:
        print("tam giac deu")
    elif a==b or b==c or c==a :
        print("tam giac can")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("tam giac vuong")
    else:
        print("tam giac thuong")