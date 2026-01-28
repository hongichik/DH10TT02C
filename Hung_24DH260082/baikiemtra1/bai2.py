PIN="hwng"
solan = 1

while solan <= 3:
    nhap = input("Nhap pass: ")
    if nhap == PIN:
        print("Tốt lắm nhập đúng rồi, có mỗi cái pass đừng để quên đấy !")
        break
    else:
        print("Pass ko đúng. cho 3s để viết lại.")
        solan += 1
else:
    print("Tài khoản bị khoá rồi! có mỗi cái pass cũng sai làm đc gì cho đời.")