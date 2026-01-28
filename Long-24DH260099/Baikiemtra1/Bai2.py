password_dung = "Nemchua36"
lan_nhap = 0
while lan_nhap < 3:
    pass_nhap = input(f"Nhap mat khau (lan {lan_nhap + 1}):")
    if pass_nhap == password_dung:
        print("Dang nhap thanh cong!")
        break
    else:
        print("Sai roi, nhap lai!")
        lan_nhap += 1
else:
    print("Tai khoan cua ban da bi khoa tam thoi")