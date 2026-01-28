try:
    dtb = float(input("nhap diem trung binh: "))
    if dtb < 0 or dtb > 10:
        print("Vui long nhap tu 0 den 10")
    if dtb >= 8.5:
        xl ="hoc sinh gioi"
    elif dtb >= 7:
        xl ="hoc sinh kha"
    elif dtb >= 5:
        xl ="hoc sinh trung binh"
    else:
        xl="Hoc sinh yeu"

    print("nhap diem trung binh : ",xl)
except ValueError:
    print("Vui long nhap so hop le trong khoang 0-10")