matkhau_dung = "Python123"
solannhap = 0
while solannhap < 3:
    matkhau = input("Nhap mat khau: ")

    if matkhau == matkhau_dung:
        print("Dang nhap thanh cong")
        break
    else:
        print("Mat khau sai, vui long nhap")
        solannhap += 1
else:
    print("Tai khoan cua ban da bi khoa tam thoi")