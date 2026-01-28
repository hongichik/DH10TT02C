password_dung = "Python123"
lan_nhap = 0
while lan_nhap < 3:
    password = input("Nhập mật khẩu: ")
    lan_nhap += 1
    if password == password_dung:
        print("Đăng nhập thành công!")
        break
    else:
        print("Mật khẩu sai, vui lòng nhập lại!")
else:
    print("Tài khoản của bạn đã bị khóa tạm thời")