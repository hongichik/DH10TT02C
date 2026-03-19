#Quan ly kho hang
Kho = {"apple": 50, "banana": 30, "orange": 20}
Kho["banana"]=10
Kho["grape"]=15
total = sum(Kho.values())
print("Tong so luong:",total)


#Danh ba dien thoai
# Tạo danh bạ
phone_book = {"An": "0901234567", "Binh": "0912345678", "Cuong": "0923456789" }
# Kiểm tra Binh
if "Binh" in phone_book:
    print("SĐT của Binh:", phone_book["Binh"])
# Xóa Cuong
phone_book.pop("Cuong")
# In danh bạ
print("Danh bạ:", phone_book)
