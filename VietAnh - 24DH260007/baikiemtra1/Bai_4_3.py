#Quan li diem so
Diem_so = [8.5, 7.0, 9.0, 6.5, 8.0]
print(Diem_so)
dtb = sum(Diem_so) / len(Diem_so)
print("Diem trung binh:" ,dtb)
Diem_so.append(7.5)
print("Danh sach sau khi them:" ,Diem_so)
Diem_so.remove(min(Diem_so))
print("Danh sach sau khi xoa diem thap nhat:" ,Diem_so)


#Danh sach mua sam
Mua_sam = ["sua", "banhmi", "trung", "nuoc"]
print(Mua_sam)
Mua_sam.insert(1 ,"gao")
print("Danh sach sau khi them:",Mua_sam)
if "trung" in Mua_sam:
    print("Co trung!")
Mua_sam.sort()
print("Danh sach sau khi sap xep:",Mua_sam)


#Ghep danh sach
Danhsach1 = [1,2,3]
Danhsach2 = [4,5,6]
merged_Danhsach = Danhsach1 + Danhsach2
print("Danh sach sau khi ghep:" ,merged_Danhsach)
#nhandoiphantu
double_Danhsach =[]
for i in merged_Danhsach:
    double_Danhsach .append(i * 2)
print("Danh sach sau khi nhan doi:",double_Danhsach)


#Thong tin sinh vien
student = {
    "id": "SV001",
    "name": "An",
    "age": "20",
    "gpa": 8.5
}
student["major"]= "CNTT"
student["gpa"] += 0.5
for key, value in student.items():
    print(key,":",value)


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


#Danh sach sinh vien
# Tạo danh sách
students = [
    {"name": "An", "age": 20, "score": 8.0},
    {"name": "Binh", "age": 21, "score": 7.5},
    {"name": "Cuong", "age": 19, "score": 9.0}
]
# Tìm sinh viên điểm cao nhất
top_student = max(students, key=lambda x: x["score"])
print("Sinh viên điểm cao nhất:", top_student)
# Tăng tuổi tất cả
for s in students:
    s["age"] += 1

print("Danh sách sau khi tăng tuổi:", students)


#Quan ly diem lop hoc
# Tạo dictionary
subjects = {
    "Toan": [8.0, 7.5, 9.0],
    "Ly": [6.5, 8.5, 7.0]
}
# Tính điểm trung bình từng môn
for subject, scores in subjects.items():
    avg = sum(scores) / len(scores)
    print(f"Điểm TB {subject}: {avg}")
# Thêm môn Hóa
subjects["Hoa"] = [7.0, 8.0, 6.5]
# In lại dictionary
print("Danh sách môn học:", subjects)