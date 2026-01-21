try :
    dtb = int (input("Nhap diem trung binh: "))
    if dtb >=8.5 :
        print ("hoc sinh gioi.")
    elif dtb >=7 :
        print ("Hoc sinh kha.")
    elif dtb >=5 :
        print ("hoc sinh trung binh.")
    else:
        print ("hoc sinh yeu.")
except ValueError :
    print("Vui long nhap lai.")