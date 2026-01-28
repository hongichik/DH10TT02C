a = float(input ("Nhap canh a: "))
b = float(input ("Nhap canh b: "))
c = float(input ("Nhap canh c: "))

if a + b > c and a + c > b and b + c > a:
    print("Đây là tam giác hợp lệ!")
    if a == b == c:
        print("Tam giác đều")
    elif a == b or b == c or a == c:
        print("Tam giác cân")
    elif a*a+b*b > c*c  or a*c+b*c > b*b or b*b+c*c > a:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")


