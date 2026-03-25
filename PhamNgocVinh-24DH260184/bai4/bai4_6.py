# Tạo danh bạ
phone_book = {
    "An": "0901234567",
    "Binh": "0912345678",
    "Cuong": "0923456789"
}

# Kiểm tra "Binh"
if "Binh" in phone_book:
    print("Số điện thoại của Binh là:", phone_book["Binh"])
else:
    print("Không tìm thấy Binh")

# Xóa "Cuong"
del phone_book["Cuong"]

# In danh bạ sau khi cập nhật
print("\nDanh bạ sau khi cập nhật:")
for name, phone in phone_book.items():
    print(name, ":", phone)