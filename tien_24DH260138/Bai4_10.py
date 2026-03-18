# Tạo dictionary môn học
lop = {
    "Toan": [8.0, 7.5, 9.0],
    "Ly": [6.5, 8.5, 7.0]
}

# Tính điểm trung bình từng môn
for mon, diem in lop.items():
    dtb = sum(diem) / len(diem)
    print(f"Điểm trung bình môn {mon}:", dtb)

# Thêm môn Hóa
lop["Hoa"] = [7.0, 8.0, 6.5]

# In lại dictionary
print("Danh sách môn học sau khi cập nhật:")
for mon, diem in lop.items():
    print(mon, ":", diem)