n = int(input("Số lượng phần tử trong danh sách: "))
so_list = []
for i in range(n):
    so = int(input("Nhập phần tử thứ {}: ".format(i + 1)))
    so_list.append(so)

for so in so_list:
    if so < 0:
        print("Mảng này có số âm tại vị trí:", so_list.index(so))
        break
else:
    print("Mảng này không có số âm, tức là mảng toàn số dương")