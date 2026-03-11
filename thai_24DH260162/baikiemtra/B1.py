a = int(input("nhập cạnh a: "))
b = int(input("nhập cạnh b: "))
c = int(input("nhập cạnh c: "))
if (a + b <= c) or (b + c <= a) or (a + c <= b):
    print("Khong phai tam giac")
else:
    if a == b == c :
        print("Tam giác đều")
    elif a == b or b == c or a == c:
        print("Tam giác cân")
    elif a^2 + b^2 == c^2 or a^2 + c^2 == b^2 or b^2 + c^2 == a^2:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
