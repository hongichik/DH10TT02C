a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    print("Đây là tam giác hợp lệ")
    if a == b == c:
        print("Là tam giác đều")
    elif a == b or a == c or b == c:
        print("Là tam giác cân")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Là tam giác vuông")
    else:
        print("Là tam giác thường")
else:
    print("Không phải tam giác")
