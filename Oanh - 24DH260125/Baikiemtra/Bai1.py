a = int(input("Nhập cạnh thứ 1 :"))
b = int(input("Nhập cạnh thứ 2 :"))
c = int(input("Nhập cạnh thứ 3 :"))
if (a+b>c) and (a+c>b) and (b+c>a):
    if a == b == c:
        print("Tam giác đều")
    elif a == b or b == c or c == a:
        print("Tam giác cân")
    elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
else:
    print("Đây không phải tam giác")