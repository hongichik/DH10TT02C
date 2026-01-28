sokm = float(input("Nhap so km da di: "))
phimocua = 10000
giamgia = 0.05
if sokm <=0 :
    print("So km khong hop le")
else:
    if sokm <= 0.8:
        print("So tien phai tra: ", phimocua, "VND" )
    elif sokm <= 30:
        print("So tien phai tra: ", phimocua + (sokm - 0.8) * 15000, "VND" )
    else:
        if sokm > 50:
            sotiengiam = (phimocua + (sokm - 0.8) * 12000) * giamgia
            tiencuoc = phimocua + (sokm - 0.8) * 12000
            print("So tien phai tra: ", tiencuoc-sotiengiam, "VND" )
        else:
            print("So tien phai tra: ", phimocua + (sokm - 0.8) * 12000, "VND" )