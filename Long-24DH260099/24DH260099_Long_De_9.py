def nhap_mhoc():
    ma = input("Nhap ma mon : ")
    ten = input("Nhap ten mon : ")
    tc = int(input("Nhap so tin chi: "))
    mon_hoc = {"maMH": ma, "tenMH": ten, "soTC": tc}
    return mon_hoc

def tong_tinchi(mhoc):
    if len(mhoc) == 0:
        return 0

    tong_tc = 0
    for mh in mhoc:
        tong_tc = tong_tc + mh["soTC"]
    return tong_tc

def loc_mhoc(mhoc, tinchi_min=2):
    ds_loc = []
    for mh in mhoc:
        if mh["soTC"] >= tinchi_min:
            ds_loc.append(mh)
    return ds_loc

print(" Nhap 3 Mon Hoc ")
danh_sach_mh = []

for i in range(3):
    print(f"Mon Hoc Thu {i + 1}:")
    mh_moi = nhap_mhoc()
    danh_sach_mh.append(mh_moi)
tong = tong_tinchi(danh_sach_mh)
print("Tong so tin chi:", tong)
ds_mh_nang = loc_mhoc(danh_sach_mh, 3)
print("Danh sach mon hoc co so tin chi >= 3:")
for mh in ds_mh_nang:
    print(mh)