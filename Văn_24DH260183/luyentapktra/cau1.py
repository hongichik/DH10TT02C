def tim_day_con(day):
    ket_qua = []

    for so in day:
        if so not in ket_qua:
            ket_qua.append(so)

    return ket_qua


# Nhập dữ liệu
n = int(input("Nhập số lượng phần tử: "))
day = []

for i in range(n):
    so = int(input("Nhập số: "))
    day.append(so)

# In kết quả
print("Dãy con là:", tim_day_con(day))