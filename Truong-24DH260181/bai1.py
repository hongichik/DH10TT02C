try:
    dtb = float(input("Nhap diem tb:"))
    if dtb < 0 or dtb > 10:
        print("Loi: Diem phai nam trong khoang 0 - 10")
        if dtb >= 8.5:
            xl ="Hoc sinh gioi"
        elif dtb >= 7:
            xl ="Hoc sinh kha"
        elif dtb >= 5:
            xl ="Hoc sinh trung binh"
        else:
            xl ="Hoc sinh yeu"
        print("Nhap diem trung binh:",xl)
except ValueError:
    print("Loi: Vui long nhap mot so hop le")
