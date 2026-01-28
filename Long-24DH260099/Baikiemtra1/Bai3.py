try:
    n = int(input("Nhap vao mot so nguyen duong (n > 1): "))
    if n <= 1:
        print("Vui long nhap so lon hon 1")
    else:
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} khong phai so nguyen to")
                break
        else:
            print(f"{n} la so nguyen to")
except ValueError:
    print("Vui long nhap mot so nguyen!")