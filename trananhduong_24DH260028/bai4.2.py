diemso = [8.5, 7.0, 9.0, 6.5, 8.0]
print(sum(diemso)/len(diemso))
diemso.append(7.5)
print(diemso)
diem_thap_nhat = min(diemso)
diemso.remove(diem_thap_nhat)
print(diemso)