So = int(input("Nhap mot so nguyen duong n: "))
if So>1:
    for i in range(2, So-1):
        if So%1 == 0:
            print("Khong phai la so nguyen to")
            break
        else:
            print("La so nguyen to")