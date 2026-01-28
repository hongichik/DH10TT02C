try:
    dtb = int(input("Nhập điểm sinh viên: "))
    print(dtb)
except ValueError:
    print("Giá trị nhập vào không phải số nguyên!")
    print("Giá trị nhập vào phải nhỏ hơn 10.")
if dtb >= 8.5 :
    print("Học sinh giỏi.")
elif dtb >= 7 :
    print("Học sinh khá.")
elif dtb >= 5 :
    print("Học sinh trung bình")
else:
    print("Học sinh yếu")   