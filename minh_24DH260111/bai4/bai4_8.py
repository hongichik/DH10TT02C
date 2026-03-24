# Tạo dictionary ban đầu
scores = {
    "Toán": [8.0, 7.5, 9.0],
    "Lý": [6.5, 8.5, 7.0]
}

# Tính điểm trung bình từng môn
print("Điểm trung bình từng môn:")
for subject, marks in scores.items():
    avg = sum(marks) / len(marks)
    print(f"{subject}: {avg:.2f}")

# Thêm môn Hóa
scores["Hóa"] = [7.0, 8.0, 6.5]

# In dictionary sau cập nhật
print("\nDanh sách sau khi thêm môn Hóa:")
for subject, marks in scores.items():
    print(f"{subject}: {marks}")
