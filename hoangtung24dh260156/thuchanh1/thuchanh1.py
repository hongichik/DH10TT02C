def tim_day_con(arr):
    result = []
    for x in arr:
        if x not in result:
            result.append(x)
    return result

# Nhập dữ liệu
n = int(input("Nhập số phần tử: "))
arr = []

for i in range(n):
    x = int(input(f"Nhập phần tử {i}: "))
    arr.append(x)

# Gọi hàm
kq = tim_day_con(arr)
print("Dãy không trùng:", kq)