#Tạo một dictionnary chứa một tt
sinh_vien={
    "id":"SV001",
    "name":"AN",
    "age":20,
    "gpa":8.5,
}
#Thêm thông tin major vs giá tri "CNTT"
print(sinh_vien)
sinh_vien["major"]="CNTT"
print(sinh_vien)
#Tăng gpa lên 0,5
sinh_vien["gpa"]+= 0.5
print(sinh_vien)
#In tất cả key và value
for key ,value in sinh_vien.items():
    print(key,":",value)