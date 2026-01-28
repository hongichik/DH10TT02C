a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Tam giac deu")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a :
        print("Tam giac vuong")
    elif a == b or a == c or b == c :
        print("Tam giac can")
    else:
        print("Tam giac thuong")
else:
 print("Khong phai tam giac")
 #bai1
    
   