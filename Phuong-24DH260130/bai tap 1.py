try:
    dtb = int(input("Nhập điểm trung bình (ĐTB) của sinh viên: "))
    if dtb < 0 or dtb > 10:
        raise ValueError("Điểm phải nằm trong khoảng từ 0 đến 10")
    if dtb >= 8.5:
        print("Học sinh giỏi")
    elif dtb >= 7.0:
        print("Học sinh khá")
    elif dtb >= 5.0:
        print("Học sinh trung bình")
    else:
        print("Học sinh yếu")
except ValueError:
    print("Lỗi: Vui lòng nhập 1 số hợp lệ trong khoảng 0-10.")

