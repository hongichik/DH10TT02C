# Tạo danh sách sinh viên
students = [
    {"name": "An", "age": 20, "score": 8.0},
    {"name": "Binh", "age": 21, "score": 7.5},
    {"name": "Chi", "age": 19, "score": 9.0}
]

# Tìm sinh viên có điểm cao nhất
top_student = max(students, key=lambda x: x["score"])
print("Sinh viên có điểm cao nhất:")
print(top_student)

# Tăng tuổi tất cả sinh viên lên 1
for student in students:
    student["age"] += 1

print("\nDanh sách sau khi tăng tuổi:")
for student in students:
    print(student)