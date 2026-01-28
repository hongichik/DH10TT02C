password = "3==D"
lan_thu = 0
max_lan = 3
while lan_thu < max_lan:
    nhap = input(f"Nhập mật khẩu (Lần {lan_thu + 1}): ")

    if nhap == password:
        print("Đăng nhập thành công!")
        break
    else:
        print("Mật khẩu sai, vui lòng nhập lại!")
        lan_thu += 1
else:
    print("Tài khoản của bạn đã bị khóa tạm thời")
    #bai2..