def nhap_sanpham():
    print("Nhập thông tin sản phẩm:")
    maSP = input("Nhập mã sản phẩm: ")
    tenSP = input("Nhập tên sản phẩm: ")

    while True:
        try:
            gia = float(input("Nhập giá sản phẩm: "))
            if gia < 0:
                print("Giá không hợp lệ, nhập lại!")
            else:
                break
        except:
            print("Vui lòng nhập số!")

    sanpham = {
        "maSP": maSP,
        "tenSP": tenSP,
        "gia": gia
    }
    return sanpham
