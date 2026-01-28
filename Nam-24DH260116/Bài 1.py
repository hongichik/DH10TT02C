try:
    dtb = int(input("Nhập điểm trung bình: "))
    if dtb <0 or dtb >10:
     raise ValueError("")
    else:
        if dtb >= 8.5:
            Loai = "Học sinh giỏi"
        elif dtb >= 7:
            Loai = "Học sinh khá"
        elif dtb >= 5:
            Loai = "học sinh trung bình"
        else:
            Loai = "Học sinh yếu"

        print("Xếp loại: ",Loai)
except ValueError:
    print("Vui lòng nhập số hợp lệ")