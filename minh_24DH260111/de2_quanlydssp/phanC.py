def loc_SP(ds_san_pham, gia=20000) :
    for sp in ds_san_pham:
        if sp['gia'] >= gia:
            print (f"Sản phẩm (sp['tenSP']) có giá {sp('gia']} lớn hơn hoặc bằng (gia)")
            DS_SP = nhap_ds _san_pham()
            hien_thi_ds_san_pham(DS_SP)
            print( f"Giá trung bình của các sản phẩm: (gia_TB(DS_SP) }")
            loc_SP(DS_SP, 30000)
