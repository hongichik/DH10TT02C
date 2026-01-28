password = "Python123"
count = 0

while count < 3:
    mk = input("Nhập mật khẩu: ")
    if mk == password:
        print("Đăng nhập thành công!")
        break
    else:
        print("Mật khẩu sai, vui lòng nhập lại!")
        count += 1
else:
    print("Tài khoản của bạn đã bị khóa tạm thời")