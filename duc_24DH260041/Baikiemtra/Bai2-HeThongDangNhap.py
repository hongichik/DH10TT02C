password = 'Python123'
count = 0

while count < 3:
    dangnhap = input('Nhap mat khau')
    if(dangnhap == password):
        print('Dang nhap thanh cong!')
        break
    else:
        print('Nhap mat khau sai! Vui long nhap lai')
        count += 1
else:
    print('Ban da nhap sai qua 3 lan, tai khoan cua ban da bi khoa tam thoi')
