#List
trai_cay = ["Chuoi","buoi","cam","dao","tao"]
print(trai_cay)
trai_cay.append("dudu")
print(trai_cay)
trai_cay[1]="nho"
print(trai_cay)
trai_cay.remove(trai_cay[5])
print(trai_cay)
trai_cay.pop(len(trai_cay)-1)
print(trai_cay)



#dictionary
ca_nhan = {
    "ten": "Thay Hong",
    "tuoi": 20,
    "nghe_nghiep": "Giảng viên",
}
print(ca_nhan)
ca_nhan["email"] = "phamnguyenhong@daihochalong.edu.vn"
print(ca_nhan)
ca_nhan["tuoi"] = 25
print(ca_nhan)
ca_nhan.pop("nghe_nghiep")
print(ca_nhan)



#1 Quan ly diem so
diem=[10,9,8,7,6]
print(diem)
diemTrungBinh=sum(diem)/len(diem)
print("Diem Trung Binh",diemTrungBinh)
diem.append(7.5)
print("Sau khi them",diem)
diemThapNhat=min(diem)
#Chỉ xóa 1 số nếu có 2 số min
diem.remove(diemThapNhat)
print("Sau khi xoa thap nhat",diem)



#2 Danh sach mua sam
canMua=["Bang vs","Gugugaga","Pipilapu","Buoi to"]
print(canMua)
canMua[1]="Gao Ngon Ngon"
print(canMua)
if "Trung" in canMua:
    print("Co Trung")
else:
    print("Khong Co Trung")
canMua.sort()
print(canMua)



#3 Ghep danh sach
ds1=[1,2,3]
print(ds1)
ds2=[4,5,6]
print(ds2)
ds3=ds1 + ds2
print("Danh sach sau khi ghep ca 2 lai",ds3)
for i in range(len(ds3)):
    ds3[i]*=2
print("Danh sach sau khi nhan 2",ds3)



#4 Thong tin sinh vien
sinhVien={
    "id":"SV01",
    "name":"Dat",
    "age":20,
    "gpa":9.5
}
#in ra gia tri vua nhap
for key,value in sinhVien.items():
    print(key,":",value)
#hien thi kieu nhu nhap vao, ca {}
print(sinhVien)
#Them nghanh hoc
sinhVien["major"]="CNTT"
#Tang diem trung binh 0.5
sinhVien["gpa"]+=0.5
#in tat ca cac key va value
for key,value in sinhVien.items():
    print(key,":",value)



#5 Quan ly kho hang
kho = {"apple": 50, "banana": 30, "orange": 20}
#in ra kieu 1
print("in kieu 1",kho)
#in ra kieu 2
for key,value in kho.items():
    if key =="apple":
        print("in kieu 2")
    print(key,":",value)
# Giảm banana xuống 10
kho["banana"] = 10

# Thêm grape
kho["grape"] = 15

# Tính tổng số lượng
tong = sum(kho.values())
print("Tổng số lượng:", tong)



#6 Danh ba SDT
danhba = {
    "Vu": "0986543212",
    "Binh": "0999999999",
    "Skibidi": "0445566999"
}

# Kiểm tra Binh
if "Binh" in danhba:
    print("Binh co trong danh ba")
    print("SĐT của Binh:", danhba["Binh"])

# Xóa Skibidi
del danhba["Skibidi"]

# In danh bạ
for key,value in danhba.items():
    print(key,":",value)



#7 Danh sach sinh vien
ds = [
    {"name": "An", "age": 20, "score": 8.0},
    {"name": "Binh", "age": 21, "score": 7.5},
    {"name": "Cuong", "age": 19, "score": 9.0}
]

# Tìm sinh viên điểm cao nhất
max_sv = ds[0]
for sv in ds:
    if sv["score"] > max_sv["score"]:
        max_sv = sv

print("Sinh viên điểm cao nhất:", max_sv)

# Tăng tuổi tất cả lên 1
for sv in ds:
    sv["age"] += 1

print("Danh sách sau khi tăng tuổi:", ds)



#8 Quan ly diem lop hoc
lop = {
    "Toan": [8.0, 7.5, 9.0],
    "Ly": [6.5, 8.5, 7.0]
}
#in kieu 1
print(lop)
#in kieu 2
for mon, diem in lop.items():
    print(mon, ":", diem)

# Tính điểm trung bình từng môn
for mon, diem in lop.items():
    dtb = sum(diem) / len(diem)
    print(mon, ":", dtb)

# Thêm môn Hóa
lop["Hoa"] = [7.0, 8.0, 6.5]

# In lại dictionary
for mon, diem in lop.items():
    print(mon, ":", diem)