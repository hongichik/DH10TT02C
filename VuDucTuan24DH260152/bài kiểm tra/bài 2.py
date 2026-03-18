pass_dung = "python123"
lan_thu = 0

while lan_thu < 3:
    nhapMK = input("Nhập mật khẩu: ")
    if nhapMK == pass_dung:
        print("Đăng nhập thành công")
        break
    else:
        print("Đăng nhập ko thành công")
        lan_thu += 1
else:
    print("Bị khóa tài khoản rồi Lmao")