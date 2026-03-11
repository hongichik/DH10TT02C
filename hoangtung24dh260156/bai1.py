try :
    dtb = int(input("nhập số điểm trung bình : "))
    if dtb >= 8.5 :
        print ("Học sinh giỏi")
    elif dtb >= 7 :
        print ("Học sinh khá")
    elif dtb >= 5 :
        print ("Học sinh trung bình")
    elif dtb >= 2 :
        print ("Học Sinh yếu")
except ValueError:
    print ("vui lòng nhập số hợp lệ")
