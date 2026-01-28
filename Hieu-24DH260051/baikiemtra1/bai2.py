password = "Python111"
count = 0
while count < 3:
    mk = input("Nhap mat khau: ")
    if mk == password:
        print("Dang nhap thanh cong!")
        break
    else:
        print("Mat khau sai, vui long nhap lai!")
        count += 1
else:
    print("Tai khoan cua ban da bi khoa tam thoi")
    