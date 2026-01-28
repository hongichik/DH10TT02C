a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

# Kiểm tra điều kiện tam giác
if a + b <= c or a + c <= b or b + c <= a:
    print("Không phải tam giác")
else:
    # Tam giác đều
    if a == b == c:
        print("Tam giác đều")

    # Tam giác vuông
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Tam giác vuông")

    # Tam giác cân
    elif a == b or a == c or b == c:
        print("Tam giác cân")

    # Còn lại
    else:
        print("Tam giác thường")
