# Tạo dictionary
sv = {
    "id": "SV001",
    "name": "An",
    "age": 20,
    "gpa": 8.5
}

# Thêm ngành học
sv["major"] = "CNTT"

# Tăng GPA
sv["gpa"] += 0.5

# In toàn bộ key - value
for key, value in sv.items():
    print(key, ":", value)