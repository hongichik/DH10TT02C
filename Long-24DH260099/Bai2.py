count = 0
danh_sach_3 = []
for i in range(1, 101):
    if i % 3 == 0:
        danh_sach_3.append(i)
        count += 1
# 3. In kết quả ra màn hình
print("Cac so chia het cho 3 tu 1 den 100 la:")
print(*danh_sach_3, sep=", ")
print(f"\n=> Co tat ca {count} so chia het cho 3.")