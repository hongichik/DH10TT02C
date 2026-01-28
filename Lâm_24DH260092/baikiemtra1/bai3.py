n = int(input("Nhập một số nguyên dương n: "))
if n <= 1:
    print("Vui lòng nhập số lớn hơn 1.")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} không phải số nguyên tố")
            break
    else:
        print(f"{n} là số nguyên tố")