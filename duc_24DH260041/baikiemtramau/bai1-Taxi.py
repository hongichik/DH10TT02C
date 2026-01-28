km = float(input('Nhap so km:'))
if km <=0:
    print('Quang duong ban nhap khong hop le!')
else:
    if km <= 0.8:
        tien = 10000
    elif km <= 30:
        tien = 10000 + (km - 0.8)* 15000
    else:
        tien = 10000 + (30 - 0.8)* 15000 + (km - 30) * 12000

    if km > 50:
        tien *= 0.95
print('so tien phai tra la:', int(tien),'VND')
