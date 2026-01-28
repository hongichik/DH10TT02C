while True:
    try:
        print("Nhap diem trung binh:", end=" ")
        dtb = float(input())
        if dtb < 0 or dtb > 10:
            raise ValueError("Diem tb phai trong khoang tu 0 den 10")
        if dtb >= 8.5:
            xl = "Gioi"
        elif dtb >= 7.0:
            xl = "Kha"
        elif dtb >= 5.0:
            xl = "Trung Binh"
        else:
            xl = "Yeu"
        print("Xep loai hoc luc: ", xl)
        break
    except ValueError:
        print("Vui long nhap diem hop le")
