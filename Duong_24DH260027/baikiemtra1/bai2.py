mkdung = "123"
lanthu = 3
while lanthu > 0:
    nhapmk = input("Nhập mật khẩu: ")
    if nhapmk == mkdung:
        print("Đăng nhập thành công")
        break
    else:
        lanthu -= 1
        print(f"Mật khẩu sai, còn {lanthu} lần thử, vui lòng nhập lại")
else:
    print("Tài khoản của bạn đã bị khóa tạm thời")