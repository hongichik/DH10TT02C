def nhap_san_pham():
    san_pham = {}
    print("Nhập thông tin sản phẩm:")
    san_pham["maSP"] = input("Mã sản phẩm: ")
    san_pham["tenSP"] = input("Tên sản phẩm: ")
    try:
        san_pham["gia"] = int(input("Giá sản phẩm: "))
    except ValueError:
        print("Giá sản phẩm phải là một số nguyên. Vui lòng nhập lại.")
        san_pham["gia"] = int(input("Giá sản phẩm: "))
    return san_pham


def nhap_ds_san_pham():
    ds_san_pham = []
    try:
        n = int(input("Nhập số lượng sản phẩm: "))
    except ValueError:
        print("Số lượng sản phẩm phải là một số nguyên. Vui lòng nhập lại.")
        n = int(input("Nhập số lượng sản phẩm: "))
    n = int(input("Nhập số lượng sản phẩm: "))
    for i in range(n):
        print(f"Sản phẩm {i+1}:")
        sp = nhap_san_pham()
        ds_san_pham.append(sp)
    return ds_san_pham


def hien_thi_ds_san_pham(ds_san_pham):
    print("Danh sách sản phẩm:")
    for sp in ds_san_pham:
        print(f"Mã SP: {sp['maSP']}, Tên SP: {sp['tenSP']}, Giá: {sp['gia']}")


# Phần B
def gia_TB(ds_san_pham):
    if len(ds_san_pham) == 0:
        return 0
    # tong_gia = sum(sp['gia'] for sp in ds_san_pham)
    tong_gia = 0
    for sp in ds_san_pham:
        tong_gia += sp['gia']
    return tong_gia / len(ds_san_pham)


# Phần C
def loc_SP(ds_san_pham, gia=20000):
    for sp in ds_san_pham:
        if sp['gia'] >= gia:
            print(f"Sản phẩm {sp['tenSP']} có giá {sp['gia']} lớn hơn hoặc bằng {gia}")

def nhap_san_pham():
    san_pham = {}
    print("Nhập thông tin sản phẩm:")
    san_pham["maSP"] = input("Mã sản phẩm: ")
    san_pham["tenSP"] = input("Tên sản phẩm: ")
    
    # Bắt lỗi giá
    while True:
        try:
            san_pham["gia"] = int(input("Giá sản phẩm: "))
            break
        except ValueError:
            print("Giá sản phẩm phải là số nguyên. Nhập lại!")
    
    return san_pham


def nhap_ds_san_pham():
    ds_san_pham = []
    
    # Bắt lỗi số lượng
    while True:
        try:
            n = int(input("Nhập số lượng sản phẩm: "))
            break
        except ValueError:
            print("Số lượng phải là số nguyên. Nhập lại!")
    
    for i in range(n):
        print(f"Sản phẩm {i+1}:")
        sp = nhap_san_pham()
        ds_san_pham.append(sp)
    
    return ds_san_pham


def hien_thi_ds_san_pham(ds_san_pham):
    print("Danh sách sản phẩm:")
    for sp in ds_san_pham:
        print(f"Mã SP: {sp['maSP']}, Tên SP: {sp['tenSP']}, Giá: {sp['gia']}")


def gia_TB(ds_san_pham):
    if len(ds_san_pham) == 0:
        return 0
    
    tong = 0
    for sp in ds_san_pham:
        tong += sp['gia']
    
    return tong / len(ds_san_pham)


def loc_SP(ds_san_pham, gia=20000):
    print(f"Sản phẩm có giá >= {gia}:")
    for sp in ds_san_pham:
        if sp['gia'] >= gia:
            print(f"{sp['tenSP']} - {sp['gia']}")


# ✅ HÀM LƯU FILE TXT
def luu_file_txt(ds_san_pham, ten_file="sanpham.txt"):
    with open(ten_file, "w", encoding="utf-8") as f:
        f.write("DANH SÁCH SẢN PHẨM\n")
        for sp in ds_san_pham:
            f.write(f"Mã SP: {sp['maSP']}, Tên SP: {sp['tenSP']}, Giá: {sp['gia']}\n")
        
        # lưu thêm giá trung bình
        f.write(f"\nGiá trung bình: {gia_TB(ds_san_pham)}\n")


# ===== CHƯƠNG TRÌNH CHÍNH =====
DS_SP = nhap_ds_san_pham()

hien_thi_ds_san_pham(DS_SP)

print(f"Giá trung bình: {gia_TB(DS_SP)}")

loc_SP(DS_SP, 30000)

# 👉 Lưu file
luu_file_txt(DS_SP)
print("Đã lưu file sanpham.txt")
DS_SP = nhap_ds_san_pham()
hien_thi_ds_san_pham(DS_SP)
print(f"Giá trung bình của các sản phẩm: {gia_TB(DS_SP)}")
loc_SP(DS_SP, 30000)
