#Tạo danh bạ
danh_ba={
    "AN":"0901234567",
    "Bình":"0912345678",
    "Cuong":"09223456789",
}
#Kiểm tra "Bình"
if "Bình" in danh_ba:
    print(danh_ba["Bình"])
#Xóa Cuong
danh_ba.pop("Cuong")
print(danh_ba)
#In danh bạo sau khi cập nhập
print(danh_ba)
for name,danh in danh_ba.items():
    print(danh)