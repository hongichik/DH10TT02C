ds_sv=[
    { "ten": "An","tuoi": 20, "diem": 8.0 },
    { "ten": "Binh", "tuoi": 21, "diem": 7.5 },
    { "ten": "Cuong", "tuoi": 19, "diem": 9.0 }
]
max_sv = ds_sv[0]
for sv in ds_sv:
    if sv["diem"]> max_sv["diem"]:
        max_sv = sv
print("sinh vien co diem cao nhat:",max_sv)
for sv in ds_sv:
    sv["tuoi"] +=1
print("danh sach sau khi tang tuoi:")
for sv in ds_sv:
    print(sv)