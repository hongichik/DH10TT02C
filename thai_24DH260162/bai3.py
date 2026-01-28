sokm = int(input("nhập số km đã đi: "))
phimocua = 10000
giamgia = 0.5
if sokm <=0:
    print("Số km không hợp lệ")
else:
    if sokm <= 0.8:
        print("số tiền phải trả: ", phimocua,"VND")
    elif sokm <= 30:
        print("số tiền phải trả:", phimocua + (sokm - 0.8) + 15000,"VND")
    else:
        if sokm >50:
            sotiengiam = ()