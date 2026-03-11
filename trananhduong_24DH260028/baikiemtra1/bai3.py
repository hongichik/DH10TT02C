So = int(input("Nhap mot so nguyen duong n: "))
if So>1:
    for i in range(2, So-1):
        if So%1 == 0:
            print(f"{So} Khong phai la so nguyen to")
            break
        else:
            print(f"{So}La so nguyen to")
    else:
        print("Vui long nhap so lon hon 1")