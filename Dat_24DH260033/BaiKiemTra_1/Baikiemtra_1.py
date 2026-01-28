a = float(input("Nhập độ dài cạnh a:"))
b = float(input("Nhập độ dài cạnh b:"))
c = float(input("Nhập độ dài cạnh c:"))
if a + b <= c or a + c <= b or b + c <= a:
    print("Không phải tam giác")
else:
    if a == b == c:
        print("Tam giác cân")
    elif a == b or b == c or c == a:
        print("Tam giác cân")
    elif a*a + b*b == c or b*b + c*c == a or a*a + c*c == b:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")