so = int(input("Nhập vào một số nguyên dương n : "))
if so > 1:
    for i in range(2, so-1 ):
        if so % i == 0:
            print(f"{so} không phải là số nguyên tố")
            break
    else:
        print(f"{so} là số nguyên tố")
else:
    print("Vui lòng nhập số lớn hơn 1")