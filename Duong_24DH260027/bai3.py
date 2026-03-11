def pt(a, b, c):
    if a!= 0:
        x = c/a
        y = 0
    elif b != 0:
        x = 0
        y = c/b
    else
        if c == 0:
            print("phuong trinh vo so nghiem")
            return
        else:
            print("phuong trinh vo so nghiem")
            return
    print("nghiem cua phuong trinh: ")
    print("x =", x)
    print("y =", y)
a = float(input("nhap a"))
b = float(input("nhap b"))
c = float(input("nhap c"))
pt(a, b, c)