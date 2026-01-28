try:
    diemTB = int(input("diemTB: "))
    if 0 <= diemTB < 10:
        print(f"Điểm trung bình đã nhập: {diemTB}")
        if diemTB >= 8:
            loai = "Giỏi"
        elif diemTB >= 6.5:
            loai = "Khá"
        elif diemTB >= 5:
            loai = "Trung Bình"
        elif diemTB >= 3:
            loai = "yếu"
        else:
            loai = "Yếu/Kém"
        print(f"xếp hạng: {loai}")
    else:
        print("Điểm cần phải ừ 0 tới 10")
except ValueError:
    print("Nhập bằng số, không phải chữ")
finally:
    print("hết")
