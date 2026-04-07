#Tạo 3 dictionary
danh_sach=[
    {"name":"An","age":20,"score":8.0,},
    {"name":"Bình","age":21,"score":9.5,},
    {"name":"Chi","age":19,"score":8.5,}
    ]
#Tìm và in thông tin sinh viên có điểm cao nhất
top_danh_sach=max(danh_sach,key=lambda x:x["score"])
# print(top_danh_sach)
#Tăng tuổi của tất cả sinh viên lên 1
for nhan_vien in danh_sach:
    nhan_vien["age"]+= 1
    print(nhan_vien)
#In danh sách mới sau khi cập nhập
print(danh_sach)
for s in danh_sach:
     print(s)