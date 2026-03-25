# Tạo hai danh sách
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Ghép hai danh sách
new_list = list1 + list2  # nối 2 list lại với nhau
print("Danh sách sau khi ghép:", new_list)

# Nhân đôi các phần tử trong danh sách
double_list = [x * 2 for x in new_list]  # dùng vòng lặp rút gọn
print("Danh sách sau khi nhân đôi:", double_list)
