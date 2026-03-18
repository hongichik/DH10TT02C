# Tạo dictionary sinh viên
sv = {
    "masv": "SV001",
    "ten": "tien",
    "tuoi": 20,
    "diem trung binh": 8.5
}

# Thêm ngành học
sv["Nganh hoc"] = "CNTT"

# Tăng điểm trung bình lên 0.5
sv["diem trung binh"] = sv["diem trung binh"] + 0.5

# In tất cả key và value
for key, value in sv.items():
    print(key, ":", value)