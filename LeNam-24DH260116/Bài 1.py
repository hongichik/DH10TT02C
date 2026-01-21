try:
    dtb = int(input("Nhập điểm trung bình: "))
    if dtb < 5:
        print("Yếu")
    elif dtb < 7:
        print("Trung bình")
    elif dtb < 8.5:
        print("Khá")
    else:
        print("Giỏi")
except ValueError:
    print("Vui lòng nhập số hợp lệ")