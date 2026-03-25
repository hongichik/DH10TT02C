# Tạo kho
kho = {
    "apple": 50,
    "banana": 30,
    "orange": 20
}

# Giảm banana xuống 10
kho["banana"] = 10

# Thêm grape
kho["grape"] = 15

# Tính tổng số lượng
tong = sum(kho.values())

# In kết quả
print("Kho hàng:", kho)
print("Tổng số lượng:", tong)