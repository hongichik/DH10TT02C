matkhau="gay"
solan = 1

while solan <= 3:
    nhap = input("Nhập mật khẩu: ")
    if nhap == matkhau:
        print("Đăng nhập thành công")
        break
    else:
        print("Đăng nhập sai. Vui lòng nhập lại.")
        solan += 1
else:
    print("Tài khoản bạn đã bị khóa tạm thời!")