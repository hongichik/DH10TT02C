n = int(input("Nhập một số nguyên dương: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Không phải là số nguyên tố")
            break
    else:
        print("Là số nguyên tố")
else:
    print("Vui lòng nhập lại số lớn hơn 1")
