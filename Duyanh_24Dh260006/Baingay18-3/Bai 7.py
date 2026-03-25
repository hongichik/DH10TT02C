# Tạo dictionary thông tin sinh viên
student = {
    "id": "SV001",
    "name": "An",
    "age": 20,
    "gpa": 8.5
}
print("Ban đầu:", student)

# Thêm ngành học
student["major"] = "CNTT"
print("Sau khi thêm major:", student)

# Tăng điểm trung bình lên 0.5
student["gpa"] = student["gpa"] + 0.5
print("Sau khi tăng GPA:", student)

# In tất cả key và value
print("Thông tin sinh viên:")
for key, value in student.items():
    print(key, ":", value)
