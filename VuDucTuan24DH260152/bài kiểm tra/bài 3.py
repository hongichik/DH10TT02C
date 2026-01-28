n = int(input("Nhập vào một số nguyên dương: "))
for i in range(2,n):
    if n % i == 0:
        print("không phải là số nguyên tố")
        break
else:
    print("là số nguyên tố")