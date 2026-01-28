try:
    a = int(input("Nhập điểm trung bình: "))
    if a < 0 or a > 10:
        raise ValueError("Điểm Không hợp lệ11")
    if a >= 8.5:
        print("Xếp loại giỏi")
    elif a >= 7:
        print("Xếp loại khá")
    elif a >= 5:
        print("Xếp loại trung bình")
    else:
        print("Xếp loại yếu")

except ValueError:
    print("Giá trị nhập không hợp lệ.")