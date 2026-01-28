password_dung = "Python123"
lan_nhap = 0
max_lan = 3
while lan_nhap < max_lan:
    nhap = input(f"Nhập mật khẩu (Lần {lan_nhap + 1}): ")
    if nhap == password_dung:
        print("Đăng nhập thành công!")
        break
    else:
        print("Mật khẩu sai, vui lòng nhập lại!")
        lan_nhap += 1
else:
    print("Tài khoản của bạn đã bị khóa tạm thời")