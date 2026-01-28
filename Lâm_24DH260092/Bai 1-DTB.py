while True:
 try:
     print("nhap diem trung binh:",end="")
     dtb = float(input())
     if dtb < 0 or dtb > 10:
        raise ValueError("Vui long  nhap so hop le tu 0 den 10 :")
     if dtb >=8 :
        xl="hoc sinh gioi"
     elif dtb >=7:
        xl="hoc sinh kha"
     elif dtb >=5:
        xl="hoc sinh trung binh"
     else:
       xl="hoc sinh yeu"

     print("xep loai hoc tap",xl)
     break
 except ValueError:
    print("Vui long  nhap so hop le tu 0 den 10 : ")
#baitap1
