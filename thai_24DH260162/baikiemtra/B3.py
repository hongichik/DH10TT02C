n = int(input("Nhập một số nguyên dương: "))
if n <= 1:
    print("vui lòng nhập 1 số lớn hơn 1. ")
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print(f"{n} không phải là số nguyên tố")
            break
    else:
        print(f"{n} là số nguyên tố: ")