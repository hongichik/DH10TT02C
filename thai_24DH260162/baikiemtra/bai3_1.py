while True:
    try:
        a = float(input("nhập hệ số a: "))
        break
    except ValueError:
        print("vui lòng nhập số.")
while True:
    try:
        b = float(input("nhập hệ số b: "))
        break
    except ValueError:
        print("vui lòng nhập số.")
if a != 0:
    x = -b / a
    print(f"phương trình có nghiệm duy nhất: x = {-b / a}")
else:
    if b == 0:
        print("phương trình có vô số nghiệm.")
    else:
        print("phương trình vô nghiệm.")