a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))
c = float(input("Nhap so c: "))

t = 0   # biến phụ

if a > b:
    t = a
    a = b
    b = t

if a > c:
    t = a
    a = c
    c = t

if b > c:
    t = b
    b = c
    c = t

print("Thu tu tang dan:", a, b, c)