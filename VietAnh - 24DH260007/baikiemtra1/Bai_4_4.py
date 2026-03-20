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
