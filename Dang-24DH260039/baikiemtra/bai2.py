password_dung = "Python123"

lan = 0

while lan < 3:
    password = input("Nhập mật khẩu: ")

    if password == password_dung:
        print("Đăng nhập thành công!")
        break
    else:
        print("Mật khẩu sai, vui lòng nhập lại!")
        lan += 1