password_dung = "Python123"
dem = 0

while dem < 3:
    password = input("Nhập mật khẩu: ")

    if password == password_dung:
        print("Đăng nhập thành công!")
        break
    else:
        print("Mật khẩu sai, vui lòng nhập lại!")
        dem += 1
else:
    print("Tài khoản của bạn đã bị khóa tạm thời")
