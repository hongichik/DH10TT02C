MK = "12345678"
lan_nhap = 0
while lan_nhap < 3:
    nhap_mk = input(f"Nhập mật khẩu (Lần {lan_nhap + 1}): ")
    if nhap_mk == MK:
        print("Chào Mừng Trở Lại")
        break#
    else:
        print("Mật khẩu không đúng" )
        lan_nhap += 1
else:
    print("Bạn đã bị khóa ")