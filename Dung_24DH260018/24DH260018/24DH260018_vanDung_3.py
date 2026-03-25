# a. Hàm nhập thông tin sản phẩm
from Dung_24DH260018.on import luu_file_txt


def nhap_sanpham():
    ma = input("Nhập mã sản phẩm: ")
    ten = input("Nhập tên sản phẩm: ")
    try:
        gia = float(input("Nhập giá sản phẩm: "))
    except ValueError:
        print("giá sản phẩm phải là số nguyên. vui lòng nhập lại.")
    gia = float(input("Nhập giá sản phẩm: "))
    san_pham = {"maSP": ma, "tenSP": ten, "gia": gia}
    return san_pham

# b. Hàm tính tổng giá
def tong_gia(sanpham):
    if len(sanpham) == 0:
        return 0

    tong = 0
    for sp in sanpham:
        tong = tong + sp["gia"]
    return tong


# c. Hàm lọc sản phẩm
def loc_sanpham(sanpham, gia_min=1000000):
    ds_loc = []
    for sp in sanpham:
        if sp["gia"] >= gia_min:
            ds_loc.append(sp)
    return ds_loc


# d. Chương trình chính
print("--- NHẬP 3 SẢN PHẨM ---")
danh_sach_sp = []
for i in range(3):
    print(f"Nhập sản phẩm thứ {i + 1}:")
    sp_moi = nhap_sanpham()
    danh_sach_sp.append(sp_moi)

tong_tien = tong_gia(danh_sach_sp)
print("Tổng giá của tất cả sản phẩm là:", tong_tien)

ds_dat_tien = loc_sanpham(danh_sach_sp, 5000000)
print("Danh sách sản phẩm có giá >= 5.000.000:")
for sp in ds_dat_tien:
    print(sp)

luu_file_txt(tong_tien)
print("đã lưu danh sách file tính tổng")