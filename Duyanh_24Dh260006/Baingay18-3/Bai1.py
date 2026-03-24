# Tạo danh sách 5 loại trái cây
fruits = ["apple", "banana", "orange", "grape", "melon"]
print("Ban đầu:", fruits)

# Thêm một loại trái cây vào cuối danh sách
fruits.append("mango")  # thêm vào cuối list
print("Sau khi thêm:", fruits)

# Thay đổi trái cây ở vị trí thứ 2 (index = 1)
fruits[1] = "mango"  # thay phần tử thứ 2
print("Sau khi thay:", fruits)

# Xóa trái cây ở vị trí cuối cùng
fruits.pop()  # xóa phần tử cuối
print("Danh sách cuối:", fruits)