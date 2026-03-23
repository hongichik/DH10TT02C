def pt(a,b,c):
    if a!=0:
        x = c/a
        y = 0
    elif b!=0:
        x = 0
        y = c/b
    else:
        if c == 0:
            print("Phuong Trinh Vo So Nghiem")
            return
        else:
            print("Puong Trinh Vo Nghiem")
            return
    print("Nghiem Cua Phuong Trinh:")
    print("x =",x)
    print("y =",y)
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

pt(a, b, c)