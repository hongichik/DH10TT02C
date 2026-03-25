def giaiptbac1(a,b):
    if a ==0 and b==0:
        print("PT vô số nghiệm ")
    elif a==0 and b!=0:
        print("PT vô nghiệm")
    else:
        print("PT có nghiệm duy nhất:",-b/a)

giaiptbac1(4,2)