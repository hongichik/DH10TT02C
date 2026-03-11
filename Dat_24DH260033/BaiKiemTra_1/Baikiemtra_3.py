songuyento = int(input("Nhập số cần kiểm tra: "))

if songuyento < 2:
    print(songuyento, "không phải là số nguyên tố")
else:
    dem = 0
    for i in range(2, songuyento):
        if songuyento % i == 0:
            dem += 1
            break
    if dem == 0:
        print(songuyento, "là số nguyên tố")
    else:
        print(songuyento, "không phải là số nguyên tố")