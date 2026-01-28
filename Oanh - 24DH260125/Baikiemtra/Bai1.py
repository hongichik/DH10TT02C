a = float(input('Nhap canh a: '))
b = float(input('Nhap canh b: '))
c = float(input('Nhap canh c: '))
if a + b + c ==0:
    print('Day khong phai la tam giac ')
else:
    if a ==b ==c:
        print('Day la tam giac deu')
    elif a == b or b == c or c == a:
        print('Day  la tam giac can ')
    elif a*a == b*b or b*b == c*c == a*a or a*a == b*b or b*b == c*c:
        print('Day  la tam giac vuong ')
    else:
        print('Day  la tam giac thuong ')
#bai1
