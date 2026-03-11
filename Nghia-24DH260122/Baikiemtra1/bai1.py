a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Không phải tam giác")
else:
    if a == b == c:
        print("Tam giác đều")
    elif (a*a + b*b == c*c) or \
         (a*a + c*c == b*b) or \
         (b*b + c*c == a*a):
        print("Tam giác vuông")
    elif a == b or a == c or b == c:
        print("Tam giác cân")
    else:
        print("Tam giác thường")
