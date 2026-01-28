n = int(input('Nhap so nguyen duong'))
if n>1:
 for i in range(2,n):
     if n%i==0:
         print('Day khong phai la so nguyen to')
         break
 else:
     print('Day la so nguyen to')
else:
    print('Day khong phai la so nguyen to')