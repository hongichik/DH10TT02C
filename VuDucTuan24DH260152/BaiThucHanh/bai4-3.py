TB = [8.5, 7.0, 9.0, 6.5, 8.0]
#tinh diem trung binh
print(sum(TB) / len(TB))
#cho 7.5 xuong cuoi
TB.append(7.5)
#xoa diem thap nhat
TB.remove(min(TB))
print(TB)
