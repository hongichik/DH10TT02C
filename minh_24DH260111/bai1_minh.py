try:
    dtb = float(input("Nhập điểm trung bình (0-10): "))

    if dtb < 0 or dtb > 10:
        raise ValueError("Điểm ngoài khoảng 0-10")

    if dtb >= 8:
        print("Xếp loại: Giỏi")
    elif dtb >= 6.5:
        print("Xếp loại: Khá")
    elif dtb >= 5:
        print("Xếp loại: Trung bình")
    else:
        print("Xếp loại: Yếu")

except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ trong khoảng 0-10")