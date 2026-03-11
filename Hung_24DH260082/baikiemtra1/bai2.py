PIN="hwng"
solan = 1

while solan <= 3:
    nhap = input("Nhap pass: ")
    if nhap == PIN:
        print("Nhập đúng rồi, có mỗi cái pass đừng để quên nhé!")
        break
    else:
        print(" Nhập sai pass rồi, cho 3s để viết lại! ")
        solan += 1
else:
    print("Tài khoản đã bị khoá, có mỗi cái pass mà cũng quên ! ")