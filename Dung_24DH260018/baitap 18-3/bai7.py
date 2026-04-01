# ================== BÀI 7: QUẢN LÝ DANH SÁCH SINH VIÊN ==================

# 1. Tạo danh sách sinh viên
students = [
    {"name": "An", "age": 20, "score": 8.0},
    {"name": "Binh", "age": 21, "score": 7.5},
    {"name": "Cuong", "age": 19, "score": 9.0}
]

# 2. Hiển thị danh sách ban đầu
print("Danh sách sinh viên ban đầu:")
for sv in students:
    print(f"Tên: {sv['name']}, Tuổi: {sv['age']}, Điểm: {sv['score']}")

# 3. Tìm sinh viên có điểm cao nhất
max_student = max(students, key=lambda sv: sv["score"])
print("\nSinh viên có điểm cao nhất:")
print(f"Tên: {max_student['name']}, Tuổi: {max_student['age']}, Điểm: {max_student['score']}")

# 4. Tăng tuổi tất cả sinh viên lên 1
for sv in students:
    sv["age"] += 1

# 5. Hiển thị danh sách sau khi tăng tuổi
print("\nDanh sách sau khi tăng tuổi:")
for sv in students:
    print(f"Tên: {sv['name']}, Tuổi: {sv['age']}, Điểm: {sv['score']}")