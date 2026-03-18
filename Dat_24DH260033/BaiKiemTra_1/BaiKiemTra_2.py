matkhau="gay"
solan = 1

while solan <= 3: # Điều kiện để khóa tài khoản
    nhap = input("Nhập mật khẩu: ")
    if nhap == matkhau:
        print("Đăng nhập thành công")
        break
    else:
        print("Đăng nhập sai. Vui lòng nhập lại.")
        solan += 1 # (While) khi sai quá nhiều
else: # Nhảy đến khi While kết thúc bằng điều kiện
    print("Tài khoản bạn đã bị khóa tạm thời!")