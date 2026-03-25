def gia_trung_binh(ds_sanpham):
    if len(ds_sanpham) == 0:
        return 0

    tong = 0
    for sp in ds_sanpham:
        tong += sp["gia"]

    return tong / len(ds_sanpham)

