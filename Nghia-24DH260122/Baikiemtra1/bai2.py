password = "Python123"
attempts = 0

while attempts < 3:
    user_input = input("Nhập mật khẩu: ")

    if user_input == password:
        print("Đăng nhập thành công!")
        break
    else:
        print("Mật khẩu sai, vui lòng nhập lại!")
        attempts += 1
else:
    print("Tài khoản của bạn đã bị khóa tạm thời")
