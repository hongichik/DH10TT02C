try :
    dtb =int(input("Nhập điểm trung bình:"))
    if dtb >=8.5 :
        print("Học sinh giỏi")
    elif dtb>=7 :
        print("Học sinh khá")
    elif dtb>=5 :
        print("Học sinh trung bình")
    else:
        print("Học sinh yếu")
except ValueError :
    print("Vui lòng nhập số hợp lế")
