a = float(input("So a: "))
b = float(input("So b: "))
print (f"{a}x + {b} = 0")
if a !=0:
    x = -b / a
    print (f"phuong trinh co 1 nghiem: x= {round(x, 2)}")
elif b == 0:
    print (f"phuong trinh vo nghiem")
else:
    print (f"phuong trinh vo so nghiem")