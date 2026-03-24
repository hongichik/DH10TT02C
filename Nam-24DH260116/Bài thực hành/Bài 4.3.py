from os import remove

danh_sach = [8.5, 7.0, 9.0, 6.5, 8.0]
print("Diem ban dau", danh_sach)
diemTB = (sum(danh_sach)/len(danh_sach))
print("điểm trung binh : ",diemTB)
danh_sach.append(7.5)
print(danh_sach)
lowest_danh_sach = min(danh_sach)
danh_sach.remove(lowest_danh_sach)
print(f"Xoa diem so thap nhat la {lowest_danh_sach}")
print("danh sach diem cuoi cung", danh_sach)