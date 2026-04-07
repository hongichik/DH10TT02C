# a. Hàm nhập thông tin môn học
def nhap_monhoc():
    ma = input("Nhập mã môn học: ")
    tc = int(input("Nhập số tín chỉ: "))
    mon_hoc = {"maMH": ma, "tenMH": ten, "soTC": tc}
    return mon_hoc


# b. Hàm tính tổng tín chỉ
def tong_tinchi(monhoc):
    if len(monhoc) == 0:
        return 0

    tong_tc = 0
    for mh in monhoc:
        tong_tc = tong_tc + mh["soTC"]
    return tong_tc


# c. Hàm lọc môn học
def loc_monhoc(monhoc, tinchi_min=2):
    ds_loc = []
    for mh in monhoc:
        if mh["soTC"] >= tinchi_min:
            ds_loc.append(mh)
    return ds_loc


# d. Chương trình chính
print("--- NHẬP 3 MÔN HỌC ---")
danh_sach_mh = []
for i in range(3):
    print(f"Nhập môn học thứ {i + 1}:")
    mh_moi = nhap_monhoc()
    danh_sach_mh.append(mh_moi)

tong = tong_tinchi(danh_sach_mh)
print("Tổng số tín chỉ là:", tong)

ds_mh_nang = loc_monhoc(danh_sach_mh, 3)
print("Danh sách môn học có số tín chỉ >= 3:")
for mh in ds_mh_nang:
    print(mh)