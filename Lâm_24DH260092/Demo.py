try:
    print("nhap diem trung binh:",end="")
    dtb = float(input())
    if dtb >0 and dtb < 10:
        raise ValueError("Vui long  nhap so hop le tu 0 den 10 :")
    if dtb >=8 :
        print("hoc sinh gioi")
    elif dtb >=7:
        print("hoc sinh kha")
    elif dtb >=5:
         print("hoc sinh trung binh")
    else:
        print("hoc sinh yeu")

    print("xep loai hoc tap")
except ValueError:
    print("Vui long  nhap so hop le tu 0 den 10 : ")