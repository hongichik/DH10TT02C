while True:
 try:
    print("Nhap Diem Trung Binh :")
    dtb = float(input())
    if dtb < 0 or dtb > 10:
        print("Loi: Diem phai nam trong khoang tu 0 den 10.")
    else:
        if dtb >= 8.5:
            xep_loai = "Gioi"
        elif dtb >= 7.0:
            xep_loai = "Kha"
        elif dtb >= 5.0:
            xep_loai = "Trung binh"
        else:
            xep_loai = "Yeu"
        print(f"ket qua xep loai:{xep_loai}")
        break
 except ValueError:
    print("Loi: Ban phai nhap diem hop le.")