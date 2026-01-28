PIN="34gh"
solan = 1

while solan <= 3:
    nhap = input("Nhap ma PIN: ")
    if nhap == PIN:
        print("Ban da dang nhap thanh cong, xin mời giao dịch!")
        break
    else:
        print("Ma PIN khong dung. Vui long thu lai.")
        solan += 1
else:
    print("Ban da nhap sai qua 3 lan, tai khoan bi khoa!")