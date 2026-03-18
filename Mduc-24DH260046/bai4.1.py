Diem=[8.5,7.8,6.7,3.6,9.0]
print("danh sach diem so goc:", Diem)
print("diem trung binh cua danh sach goc:", sum(Diem)/len(Diem))
Diem.append(8.8)
print("danh sach diem khi them vao danh sach", Diem)
Diem_thap_nhat=min(Diem)
Diem.remove(Diem_thap_nhat)
print("danh sach diem sau khi soa diem thap nhat:",Diem)
