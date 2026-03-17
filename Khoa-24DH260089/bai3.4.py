danhsach = []
n = 0

def nhap():
    global danhsach, n
    n = int(input("Nhập số lượng phần tử:"))
    for i in range(n):
        so = int(input("Nhập phần tử thứ {}:".format(i + 1)))
        for i in range(n):
            so = int(input("Nhập phần tử thứ {}:".format(i + 1)))
            danhsach.append(so)
def sapxep():
    for i in range(n):
        for j in range(i + 1, n):
            if danhsach[i] > danhsach[j]:
               danhsach[i], danhsach[j] = danhsach[j], danhsach[i]
    print("Thứ tự tăng dần:", danhsach)
def hienthi():
    for i in range(n):
        print(danhsach[i], end="")
    print()
nhap()
hienthi()
sapxep()
hienthi()