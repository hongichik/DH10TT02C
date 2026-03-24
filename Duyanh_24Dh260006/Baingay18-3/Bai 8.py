# Tạo dictionary chứa danh bạ
danh_ba = {
    "An": "0901234567",
    "Binh": "0912345678",
    "Cuong": "0923456789"
}

# Kiểm tra "Binh" có trong danh bạ không
if "Binh" in danh_ba:
    print("Số điện thoại của Bình:", danh_ba["Binh"])
else:
    print("Không tìm thấy Bình")

# Xóa thông tin của "Cuong"
if "Cuong" in danh_ba:
    del danh_ba["Cuong"]

# In danh bạ sau khi cập nhật
print("Danh bạ sau khi cập nhật:")
for ten, sdt in danh_ba.items():
    print(ten, ":", sdt)