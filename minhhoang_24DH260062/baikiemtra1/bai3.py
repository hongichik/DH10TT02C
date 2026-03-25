n = int(input("Nhập số nguyên dương n (>1): "))

if n > 1:
    # Kiểm tra từ 2 đến căn bậc hai của n để tối ưu
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} không phải là số nguyên tố")
            break
    else:
        print(f"{n} là số nguyên tố")
else:
    print("Vui lòng nhập số lớn hơn 1")