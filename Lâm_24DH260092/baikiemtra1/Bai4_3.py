#Tạo danh sách list
diem_so=[8.5,7.0,9.0,6.5,8.0]
#Tính điểm tb
diem_tb= sum(diem_so)/len(diem_so)
print(diem_tb)
#Thêm 1 điểm số 7.5
diem_so.append(7.5)
print(diem_so)
#Xóa điểm số thâấp nhất
min_diem_so=min(diem_so)
diem_so.remove(min_diem_so)
print(diem_so)