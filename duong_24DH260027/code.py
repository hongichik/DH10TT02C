while True:
    try:
        dtb = float(input("Nhập ĐTB: "))
        if dtb < 0 or dtb > 10:
            raise ValueError("Điểm phải từ 0 đến 10")
        if dtb >= 8.5:
            print("Xếp loại: Giỏi")
        elif dtb >= 7.0:
            print("Xếp loại: Khá")
        elif dtb >= 5.0:
            print("Xếp loại: Trung bình")
        else:
            print("Xếp loại: Yếu")
        break
    except ValueError as e:
        if "could not convert string" in str(e):
            print("Lỗi: Nhập sai định dạng số")
        else:
            print(f"Lỗi: {e}")
