n = int(input("Nhập số nguyên dương n (n > 1): "))

for i in range(2, n):
    if n % i == 0:
        print(n, "không phải là số nguyên tố")
        break
else:
    print(n, "là số nguyên tố")