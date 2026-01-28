PASSWORD = "vannguyen5790"

for lan in range(1, 4):
    nhap = input("Nhập mật khẩu: ")

    if nhap == PASSWORD:
        print("Đăng nhập thành công!")
        break
    else:
        print("Sai mật khẩu!")
else:
    print("Tài khoản đã bị khóa tạm thời")
