try:
    # Sửa dbt thành dtb ở đây
    dtb = float(input("Nhap diem trung binh: "))

    if dtb < 0 or dtb > 10:
        raise ValueError

    if dtb >= 8.5:
        print("Loai gioi")
    elif dtb >= 7:
        print("Loai kha")
    elif dtb >= 5:
        print("Loai trung binh")
    else:
        print("Loai yeu")

except ValueError:
    print("Vui long nhap so hop le tu 0 den 10!")