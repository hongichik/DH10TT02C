diem = [8.5, 7.0, 9.0, 6.5, 8.0]
trung_binh = sum(diem) / len(diem)
print("Điểm trung bình:", trung_binh)
diem.append(7.5)
print("Danh sách sau khi thêm:", diem)
diem.remove(min(diem))
print("Danh sách sau khi xóa điểm thấp nhất:", diem)