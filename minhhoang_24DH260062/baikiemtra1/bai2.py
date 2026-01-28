password_dung = "Python123"
lan_thu = 0

while lan_thu < 3:
    mk = input("Nhập mật khẩu: ")
    if mk == password_dung:
        print("Đăng nhập thành công!")
        break
    else:
        lan_thu += 1
        print(f"Mật khẩu sai. Bạn còn {3 - lan_thu} lần thử.")
else:
    print("Tài khoản của bạn đã bị khóa tạm thời!")