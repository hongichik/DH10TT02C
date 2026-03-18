# Tạo 2 danh sách
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Ghép 2 danh sách
list_moi = list1 + list2
print("Danh sách sau khi ghép:", list_moi)

# Nhân đôi từng phần tử
ket_qua = []
for i in list_moi:
    ket_qua.append(i * 2)

# In kết quả
print("Danh sách sau khi nhân đôi:", ket_qua)