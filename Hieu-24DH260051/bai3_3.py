danhsach = []
n = 0 

def nhap():
    global danhsach, n
    n = 3
    for i in range(n):
        sp = float(input("Nhap phan tu thu {}: ".format(i + 1)))
        danhsach.append(sp)

def sap_xep():
    global danhsach
    t = 0

    if danhsach[0] > danhsach[1]:
        t = danhsach[0]
        danhsach[0] = danhsach[1]
        danhsach[1] = t

    if danhsach[0] > danhsach[2]:
        t = danhsach[0]
        danhsach[0] = danhsach[2]
        danhsach[2] = t

    if danhsach[1] > danhsach[2]:
        t = danhsach[1]
        danhsach[1] = danhsach[2]
        danhsach[2] = t

def xuat():
    print("Ba so theo thu tu tang dan:", danhsach[0], danhsach[1], danhsach[2])

nhap()
sap_xep()
xuat()