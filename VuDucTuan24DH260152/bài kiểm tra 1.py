sokm = float(input("Nhap so KM da di: "))
phimocua = 10000
giamGia = 0.05
if sokm <=0:
    print("so km khong hop le")
else:
    if sokm <=0.8:
        print("so tien phai tra: ", phimocua, "VNĐ")
    elif sokm <=30:
        print("so tien phai tra: ", phimocua + (sokm - 0.8) * 15000, "VNĐ")
    else:
        if sokm >50:
            print ("so tien phai tra:", (phimocua+ (sokm - 0.8) * 12000) *giamGia, "VNĐ")
        else:
            print("so tien phai tra: ", phimocua +(sokm - 0.8)*1200, "VNĐ")