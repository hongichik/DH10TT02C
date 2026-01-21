try:
    ho_ten = input("Nhập họ tên sinh viên: ")
    dtb = float(input("Nhập điểm trung bình : "))
    if dtb < 0 or dtb > 10:
        print("Lỗi: Điểm phải nằm trong khoảng từ 0 đến 10!")
    else:
        if dtb >= 8.5:
            xep_loai = "Học sinh Giỏi"
        elif dtb >= 7.0:
            xep_loai = "Học sinh Khá"
        elif dtb >= 5.0:
            xep_loai = "Học sinh Trung bình"
        else:
            xep_loai = "Học sinh Yếu"
        print(f"Kết quả xếp loại: {xep_loai}")
except ValueError:
    print("Lỗi: Bạn phải nhập vào một số thực!")