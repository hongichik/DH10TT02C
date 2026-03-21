# Tạo danh sách điểm
diem = [8.5, 7.0, 9.0, 6.5, 8.0]

# Tính điểm trung bình
dtb = sum(diem) / len(diem)
print("Điểm trung bình:", dtb)

# Thêm điểm 7.5 vào cuối danh sách
diem.append(7.5)
print("Danh sách sau khi thêm:", diem)

# Xóa điểm thấp nhất
min_diem = min(diem)
diem.remove(min_diem)

print("Danh sách sau khi xóa điểm thấp nhất:", diem)