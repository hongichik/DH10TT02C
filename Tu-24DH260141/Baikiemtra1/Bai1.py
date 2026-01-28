a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Đây là tam giác đều")
    elif a == b or b == c or a == c:
        print("Đây là tam giác cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Đây là tam giác vuông")
    else:
        print("Đây là tam giác thường")
else:
    print("Đây không phải tam giác")