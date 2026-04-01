def nhap_san_pham ():
    san_pham = {}
    print("Nhập thông tin sản phẩm :")
    san_pham["MaSP"] = input("Mã Sản Phẩm")
    san_pham["TenSP"] = input ("Tên Sản Phẩm")
    san_pham["Gia"] = int(input("Giá Sản Phẩm"))
    return san_pham

def nhap_ds_san_pham():
    ds_san_pham = []
    try:
        n = int(input("Nhâp số lượng sản phẩm :"))
    except ValueError:
        print("Số lượng sản phẩm phải là 1 số nguyên. Vui lòng nhập lại. ")
        n = int(input("Nhập số lượng sản phẩm: "))
    n = int(input("Nhập số lượng sản phẩm: "))
    for i in range(n):
        print(f"Sản Phẩm {i+1}:")
        sp = nhap_san_pham()
        ds_san_pham.append(sp)
    return ds_san_pham

def hien_thi_ds_san_pham(ds_san_pham):
    print("Danh sách sản phẩm:")
    for sp  in ds_san_pham:
        print(f"MaSP:{sp['MaSP']}, TenSP:{sp['TenSP']}, Gia:{sp['Gia']}")

#Phần B
def Gia_TB(ds_san_pham):
    if len(ds_san_pham) == 0 :
        return 0
    tong_gia = 0
    for sp in ds_san_pham:
        tong_gia += sp["Gia"]
    return tong_gia / len(ds_san_pham)

#Phần C
def loc_Sp(ds_san_pham, Gia=20000):
    for sp in ds_san_pham:
        if sp['Gia'] >= Gia:
            print (f"Sản phẩm {sp['TenSP']} có giá {sp['Gia']} lớn hơn hoặc bằng {Gia}")
DS_SP = nhap_ds_san_pham()
hien_thi_ds_san_pham(DS_SP)
print(f"Giá trung bình của các sản phẩm:{Gia_TB(DS_SP)}")
loc_Sp(DS_SP, 30000)