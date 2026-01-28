password_dung = "123"
solanthu = 3
while solanthu > 0:
    nhapmatkhau = input("Nhập mật khẩu: ")
    if nhapmatkhau == password_dung:
        print("Đăng nhập thành công!")
        break
    else:
        solanthu -= 1
        if solanthu > 0:
            print(f"Mật khẩu sai, vui lòng nhập lại! (Còn {solanthu} lần thử)")
else:
    print("Tài khoản của bạn đã bị khóa tạm thời")