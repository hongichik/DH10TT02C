diemso = [8.5, 7.0, 9.0, 6.5, 8.0]
tb = sum(diemso) / len(diemso)
print("DTB: ", tb)
diemso.append(7.5)
print("Sau khi them diem: ", diemso)
diemso.remove(min(diemso))
print("Sau khi xoa diem nho nhat: ", diemso)
############################################
dsms = ["Lap xuong", "Coca", "Sanwich", "Kho ga"]
dsms.insert(1,"Gao")
print(dsms)
if "Lap xuong" in dsms:
    print("Danh sach co trung")
dsms.sort()
print("Danh sach mua sam sau khi sap xep: ", dsms)