# Nhập 3 cạnh
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra có phải tam giác không
if a + b > c and a + c > b and b + c > a:
    print("Đây là tam giác hợp lệ")

    # Tam giác đều
    if a == b and b == c:
        print("Tam giác đều")

    # Tam giác cân
    elif a == b or a == c or b == c:
        print("Tam giác cân")

    # Tam giác vuông
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Tam giác vuông")

    # Tam giác thường
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")