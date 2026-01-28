password_dung = "Python123"

lan_nhap = 0

while lan_nhap < 3:
    mk = input("Nhap mat khau: ")
    if mk == password_dung:
        print("Dang nhap thanh cong!")
        break
    else:
        print("Mat khau sai, vui long nhap lai!")
        lan_nhap += 1
else:
    print("Tai khoan cua ban da bi khoa tam thoi")