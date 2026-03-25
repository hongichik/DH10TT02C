a = float(input("nhập độ dài cạnh a: "))
b = float(input("nhập độ dài cạnh b: "))
c = float(input("nhâ đồ dài canh c: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Đây là tam giác đều")
    if a == b or b == c or c == a:
        print("đây là tam giác cân")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("đây là tam giác vuong")
    else:
        print("dây là tam giác thường")
else:
    print("dây không phải là tam giác")
