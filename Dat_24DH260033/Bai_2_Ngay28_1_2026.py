#For dùng range(begin,end,step)
# begin: Giá trị bắt đầu
# end: Giá trị cuối
# step: Bước nhảy

for n in range(1,10,2):
    print(n,end=' ')
#Xuong dong
print()
# Bai tap 1-100 bao nhieu so chia het cho 3
# k la bien dem
k=0
for n in range(1,100):
    if n % 3 == 0:
        k+=1
print("Tu 1-100 co:",k,"so chia het cho 3")