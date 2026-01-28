
count = 0
for n in range(1,101):
    if n % 3 == 0:
        count += 1
        print(f"số chia hết cho 3 tìm được:{n}")
print("_"*20)
print(f"có {count} số được tìm thấy chia hết cho 3")