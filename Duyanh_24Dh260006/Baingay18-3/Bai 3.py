# Tạo danh sách 5 điểm số
scores = [8.5, 7.0, 9.0, 6.5, 8.0]
print("Danh sách ban đầu:", scores)

# Tính điểm trung bình
average = sum(scores) / len(scores)  # sum: tổng, len: số phần tử
print("Điểm trung bình:", average)

# Thêm điểm 7.5 vào cuối danh sách
scores.append(7.5)
print("Sau khi thêm:", scores)

# Xóa điểm thấp nhất
min_score = min(scores)  # tìm giá trị nhỏ nhất
scores.remove(min_score)  # xóa giá trị nhỏ nhất
print("Sau khi xóa điểm thấp nhất:", scores)