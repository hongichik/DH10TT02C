#Phần A
def nhap_sanpham():
    san_pham = {}
    print("Nhập thông tin sản phẩm:")
    san_pham["maSP"] = input("Mã sản phẩm: ")
    san_pham["tenSP"] = input("Tên sản phẩm: ")
    san_pham["gia"] = int(input("Giá sản phẩm: "))
    return san_pham

def nhap_ds_sanpham():
    ds_sanpham = []
    n = int(input("Nhập số lượng sản phẩm: "))
    for i in range(n):
        print(f"Sản phẩm {i+1}:")
        sp = nhap_sanpham()
        ds_sanpham.append(sp)
    return ds_sanpham

def hien_thi_ds_san_pham(ds_sanpham):
    print("Danh sách sản phẩm: ")
    for sp in ds_sanpham:
        print(f"Mã SP: {sp['maSP']}, Tên SP: {sp['tenSP']}, Giá: {sp['gia']}")
#Phần B
def gia_TB(ds_sanpham):
    if len(ds_sanpham) == 0:
        return 0
    # tong_gia = sum(sp['gia'] for sp in ds_san_pham)
    tong_gia = 0
    for sp in ds_sanpham:
        tong_gia += sp["gia"]
    return tong_gia / len(ds_sanpham)
#Phần C
def loc_SP(ds_sanpham, gia = min):
    for sp in ds_sanpham:
        if sp('gia') >= gia:
            print(f"Sản phẩm {sp['tenSP']} có giá {sp['gia']} lớn hơn hoặc bằng {gia}")

DS_SP = nhap_ds_sanpham()
hien_thi_ds_san_pham(DS_SP)
print(f"Giá trung bình của các sản phẩm: {gia_TB(DS_SP)}")
loc_SP(DS_SP, gia_TB() >= 1000000)

#Phần D
def nhap_sanpham():
    san_pham = {}
    print ("Nhap 3 san pham")
    ds_sanpham = []
    for i in range(3):
        print("Nhập sản phẩm {i+1}:")
        sp_moi = nhap_sanpham()
        ds_sanpham.append(sp_moi)

    tong_gia = gia_TB(ds_sanpham)
    print("Tổng giá tất cả sản phâm")
