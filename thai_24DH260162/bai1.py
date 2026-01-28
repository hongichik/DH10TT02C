try:
    dtb = int(input("nhập điểm trung bình: "))
    if dtb < 0 or dtb > 10:
        raise ImportError("điểm phải trong khoảng từ 0-10")
    if dtb >= 8.5:
        print("học sinh giỏi")
    elif dtb >= 7:
        print("học sinh khá")
    elif dtb >= 5:
        print("học sinh trung bình")
    else:
        print("học sinh yếu")
except ImportError:
    print("Vui lòng nhập số hợp lệ trong khoảng 0-10.")
