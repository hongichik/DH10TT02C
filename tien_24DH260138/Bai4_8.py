# Tạo danh bạ
danh_ba = {
    "An": "0901234567",
    "Binh": "0912345678",
    "Cuong": "0923456789"
}

# Kiểm tra "Binh"
if "Binh" in danh_ba:
    print("Số của Binh là:", danh_ba["Binh"])
else:
    print("Không có Binh trong danh bạ")

# Xóa "Cuong"
del danh_ba["Cuong"]

# In danh bạ sau khi cập nhật
print("Danh bạ sau khi cập nhật:")
for ten, sdt in danh_ba.items():
    print(ten, ":", sdt)