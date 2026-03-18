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