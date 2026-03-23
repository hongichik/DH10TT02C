diem_lop_hoc={" Toán": [8.0, 7.5, 9.0], "Lý": [6.5, 8.5, 7.0]}
print (" Danh sách điểm ban đầu:", diem_lop_hoc)
print (" Danh sách điểm trung bình:")
for mon, ds_diem in diem_lop_hoc.items():
    trung_binh=sum(ds_diem)/len(ds_diem)
    print(f"- Môn {mon}: {trung_binh:.2f}")
diem_lop_hoc["Hóa"]=[7.0, 8.0, 6.5]
print ("Danh sách điểm sau khi thêm Hóa:", diem_lop_hoc)