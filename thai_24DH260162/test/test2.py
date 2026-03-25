PIN_DUNG = "namgay"
solan = 1
while solan <= 3:
    print("Bạn có 3 lần thử:")
    n = input("Nhập mk namgay: ")
    if n == PIN_DUNG:
        print("Mã Gay chính xác. mời bạn chọn giao dịch. ")
        break
    else:
        print(f"Mã Gay sai. bạn còn {3 -solan} lần thử")
        solan += 1
else:
    print("THẺ ĐÃ BỊ NAM GAY NUỐT. Vui lòng liên hệ ngân hàng. ")