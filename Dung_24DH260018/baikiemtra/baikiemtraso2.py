password_dung = "dungdeptrai"

so_lan = 3
while so_lan > 0:
    password_nhap = input("Nhập mật khẩu: ")

    if password_nhap == password_dung:
        print("Đăng nhập thành công!")
        break
    else:
        so_lan -= 1
        if so_lan > 0:
            print("Mật khẩu sai, vui lòng nhập lại!")
else:
    print("Tài khoản của bạn đã bị khóa tạm thời")
