try:
    dtb = float(input("Nhập điểm trung bình của sinh viên: "))
    if dtb < 0 or dtb > 10:
        raise ValueError("Điểm phải nằm trong khoảng từ 0 đến 10")
    if dtb < 5:
        hoc_luc = "Yếu"
    elif dtb < 6.5:
        hoc_luc = "Trung bình"
    elif dtb < 8:
        hoc_luc = "Khá"
    elif dtb < 9:
        hoc_luc = "Giỏi"
    else:
        hoc_luc = "Xuất sắc"
    print(f"Điểm trung bình: {dtb}")
    print(f"Xếp loại học lực: {hoc_luc}")
except ValueError as e:
    print("Lỗi!:", e)