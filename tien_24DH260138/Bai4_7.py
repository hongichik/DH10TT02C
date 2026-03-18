# Tạo kho
kho = {
    "tao": 50,
    "chuoi": 30,
    "cam": 20
}

# Giảm số lượng chuoi xuống 10
kho["chuoi"] = 10

# Thêm sản phẩm nho
kho["nho"] = 15

# Tính tổng số lượng
tong = sum(kho.values())

print("Danh sách kho:", kho)
print("Tổng số lượng sản phẩm:", tong)