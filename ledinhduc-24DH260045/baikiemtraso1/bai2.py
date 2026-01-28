password_dung = "Python123"
lan_thu = 0
max_lan = 3
while lan_thu < max_lan:
    nhap = input(f"Nhap mat khau (Lan {lan_thu + 1}): ")
    if nhap == password_dung:
        print("Dang nhap thanh cong!")
        break
    else:
        print("Mat khau sai , vui long nhap lai!")
        lan_thu += 1
else:
    print("Tai khoan cua ban bi khoa tam thoi")