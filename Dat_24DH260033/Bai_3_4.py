a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

t = 0
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