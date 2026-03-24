# Tạo danh sách sinh viên
students = [
    {"name": "An", "age": 20, "score": 8.0},
    {"name": "Binh", "age": 21, "score": 7.5},
    {"name": "Cuong", "age": 19, "score": 9.0}
]

# Tìm sinh viên có điểm cao nhất
max_student = max(students, key=lambda x: x["score"])
print("Sinh viên có điểm cao nhất:", max_student)

# Tăng tuổi tất cả sinh viên lên 1
for sv in students:
    sv["age"] += 1

# In danh sách mới
print("Danh sách sau khi tăng tuổi:")
for sv in students:
    print(sv)