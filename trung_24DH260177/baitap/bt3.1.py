a= float (input("Nhap a:"))
b= float (input("Nhap b:"))
if a==0:
    if b==0:
        print("phuong trinh vo so nghiem")
    else:
        print("phuong trinh vo nghiem")
        
else:
    x= -b /a
    print("Phuong trinh co nghiem x=",x)