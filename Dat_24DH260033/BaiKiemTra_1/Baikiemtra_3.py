songuyento = int(input("Nhập số cần kiểm tra: "))

if songuyento < 2: # Số nguyên tố bắt đầu từ 2
    print(songuyento, "không phải là số nguyên tố")
else:
    dem = 0 # Biến kiểm tra có chia hết cho số nào không
    for i in range(2, songuyento): # Vòng lặp chia lần lượt từng số
        if songuyento % i == 0:
            dem += 1
            break
    if dem == 0:
        print(songuyento, "là số nguyên tố")
    else:
        print(songuyento, "không phải là số nguyên tố")