hang_hoa = []

def them_hang():
    ma = input("Nhập mã hàng: ")
    ten = input("Nhập tên hàng: ")
    ngay = input("Nhập ngày sản xuất: ")
    loai = input("Nhập loại hàng: ")

    hang_hoa.append([ma, ten, ngay, loai])


def sua_hang():
    ma_can_sua = input("Nhập mã hàng cần sửa: ")

    for hang in hang_hoa:
        if hang[0] == ma_can_sua:
            hang[1] = input("Tên mới: ")
            hang[3] = input("Loại mới: ")
            print("Đã sửa!")
            return

    print("Không tìm thấy!")


def hien_thi():
    for hang in hang_hoa:
        print(hang)


# Menu đơn giản
while True:
    print("\n1. Thêm")
    print("2. Sửa")
    print("3. Hiển thị")
    print("0. Thoát")

    chon = input("Chọn: ")

    if chon == "1":
        them_hang()
    elif chon == "2":
        sua_hang()
    elif chon == "3":
        hien_thi()
    elif chon == "0":
        break