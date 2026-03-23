diem_mh = {
    "Toan": [8.0, 7.5, 9.0],
    "Ly": [6.5, 8.5, 7.0]
}
print("diem tb tung mon")
for mon, ds_diem in diem_mh.items(): tb = sum(ds_diem)/ len(ds_diem)
print(f"{mon}: {tb:.2f}")
diem_mh["Hoa"] = [7.0, 8.0, 6.5]
print(diem_mh)