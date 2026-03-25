# Tạo danh sách
ds = ["sữa", "bánh mì", "trứng", "nước"]

# Thêm "gạo" vào vị trí thứ 2 (index 1)
ds.insert(1, "gạo")
print("Sau khi thêm:", ds)

# Kiểm tra "trứng"
if "trứng" in ds:
    print("Có trứng")
else:
    print("Không có trứng")

# Sắp xếp
ds.sort()
print("Sau khi sắp xếp:", ds)