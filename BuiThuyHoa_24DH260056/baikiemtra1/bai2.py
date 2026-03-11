password = "noptiendi"
count = 0
while count < 3:
    mk = input("Nhập mật khẩu: ")
    if mk == password:
        print("Đăng nhập thành công!")
        break
    else:
        print("Sai mật khẩu vui lòng nhập lại!")
        count += 1
else:
        print("Tài khoản bị khóa tạm thời!")


