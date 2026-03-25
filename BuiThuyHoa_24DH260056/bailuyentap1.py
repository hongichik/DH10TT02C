#Phần A
def nhap_san_pham():
    san_pham = {}
    print("Nhập thông tin sản phẩm:")
    san_pham["maSP"] = input("Mã sản phẩm: ")
    san_pham["tenSP"] = input("Tên sản phẩm: ")
    san_pham["gia"] = int(input("Giá sản phẩm: "))
    return san_pham

def nhap_ds_san_pham():
    ds_san_pham = []
    n = int(input("Nhập số lượng sản phẩm: "))
    for i in range(n):
        print(f"Sản phẩm {i+1}:")
        sp = nhap_san_pham()
        ds_san_pham.append(sp)
    return ds_san_pham

def hien_thi_ds_san_pham(ds_san_pham):
    print("Danh sách sản phẩm: ")
    for sp in ds_san_pham:
        print(f"Mã SP: {sp['maSP']}, Tên SP: {sp['tenSP']}, Giá: {sp['gia']}")

#Phần B
def gia_TB(ds_san_pham):
    if len(ds_san_pham) == 0:
        return 0
    # tong_gia = sum(sp['gia'] for sp in ds_san_pham)
    tong_gia = 0
    for sp in ds_san_pham:
        tong_gia += sp["gia"]
    return tong_gia / len(ds_san_pham)

#Phần C
def loc_SP(ds_san_pham, gia = 20000):
    for sp in ds_san_pham:
        if sp('gia') >= gia:
            print(f"Sản phẩm {sp['tenSP']} có giá {sp[gia]} lớn hơn hoặc bằng {gia}")

DS_SP = nhap_ds_san_pham()
hien_thi_ds_san_pham(DS_SP)
print(f"Giá trung bình của các sản phẩm: {gia_TB(DS_SP)}")
loc_SP(DS_SP, 30000)