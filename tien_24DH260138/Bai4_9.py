# Tạo danh sách sinh viên
ds_sv = [
    {"name": "An", "age": 20, "score": 8.0},
    {"name": "Binh", "age": 21, "score": 7.5},
    {"name": "Cuong", "age": 19, "score": 9.0}
]

# Tìm sinh viên có điểm cao nhất
max_sv = ds_sv[0]
for sv in ds_sv:
    if sv["score"] > max_sv["score"]:
        max_sv = sv

print("Sinh viên điểm cao nhất:", max_sv)

# Tăng tuổi tất cả sinh viên lên 1
for sv in ds_sv:
    sv["age"] += 1

print("Danh sách sau khi tăng tuổi:")
for sv in ds_sv:
    print(sv)