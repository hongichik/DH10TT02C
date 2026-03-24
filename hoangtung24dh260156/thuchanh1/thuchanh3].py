hanghoa = []

def them_hang():
    ma = input("Mã hàng: ")
    ten = input("Tên hàng: ")
    ngay = input("Ngày sản xuất: ")
    loai = input("Loại hàng: ")

    hanghoa.append({
        "ma": ma,
        "ten": ten,
        "ngay": ngay,
        "loai": loai
    })

def sua_hang():
    ma = input("Nhập mã cần sửa: ")
    for h in hanghoa:
        if h["ma"] == ma:
            h["ten"] = input("Tên mới: ")
            h["loai"] = input("Loại mới: ")
            print("Đã cập nhật!")
            return
    print("Không tìm thấy!")

def hien_thi():
    for h in hanghoa:
        print(h)

# Menu
while True:
    print("\n1. Thêm hàng")
    print("2. Sửa hàng")
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