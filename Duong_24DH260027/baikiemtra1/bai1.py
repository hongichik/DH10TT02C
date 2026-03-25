a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Là tam giác đều")
    elif a == b or b == c or a == c:
        print("Là tam giác cân")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
        print("Là tam giác vuông")
    else:
        print("Là tam giác thường")
else:
    print("Không phải là tam giác")