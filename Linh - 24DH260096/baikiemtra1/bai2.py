mk = "Linh"
solan = 1

while solan <=3:
    nhap = input("Nhap mat khau: ")
    if nhap ==mk:
        print("Dang nhap thanh cong!")
        break
    else:
        print("Mat khau sai, vui long nhap lai!")
        solan +=1
else:
    print("Tai khoan cua ban da bi khoa tam thoi")