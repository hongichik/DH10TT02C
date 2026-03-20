diem_so=[8.5, 7.0, 9.0, 6.5, 8.0]
print("Danh sách điểm số ban đầu:", diem_so)
print("Điểm trung bình của danh sách ban đầu:", sum(diem_so)/len(diem_so))
diem_so.append(7.5)
print("Danh sách điểm sau khi thêm điểm vào danh sách:", diem_so)
diem_thap_nhat=min(diem_so)
diem_so.remove(diem_thap_nhat)
print("Danh sách điểm số sau khi xóa điểm thấp nhất:", diem_so)