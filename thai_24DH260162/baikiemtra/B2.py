mk = "Thainguyen"
solan = 1
while solan <= 3:
    nhap = input("nhập mật khẩu: ")
    if nhap == mk:
        print("đăng nhập thành công")
        break
    else:
        print("mật khẩu sai, vui lòng nhập lại: ")
        solan += 1
else:
    print("tài khoản của bạn đã bị khóa tạm thời: ")