a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    print("Đây là tam giác hợp lệ")

    if a == b and b == c:
        print("Tam giác đều")

    elif a == b or a == c or b == c:
        print("Tam giác cân")

    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")