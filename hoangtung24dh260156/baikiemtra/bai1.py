a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra tam giác hợp lệ
if a + b > c and a + c > b and b + c > a:
    print("Đây là tam giác hợp lệ")

    # Tam giác đều
    if a == b == c:
        print("Tam giác đều")

    # Tam giác cân
    elif a == b or a == c or b == c:
        print("Tam giác cân")

    # Tam giác vuông
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Tam giác vuông")

    # Tam giác thường
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")
