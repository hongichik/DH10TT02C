try:
# mo rong bai1 ( tinh diem hoc ki ca nam)
    chuyen_can = 10.0
    print(f"Diem chuyen can: {chuyen_can}")

#nhap diem hk1 va hk2
    print("\n--- Nhap diem Hoc ky 1 ---")
    t1 = float(input("Toan HK1: "))
    v1 = float(input("Van HK1: "))
    a1 = float(input("Anh HK1: "))

    print("\n--- Nhap diem Hoc ky 2 ---")
    t2 = float(input("Toan HK2: "))
    v2 = float(input("Van HK2: "))
    a2 = float(input("Anh HK2: "))
#kiem tra loi ngoai so 0 den 10
    tat_ca_diem = [t1, v1, a1, t2, v2, a2]
    for diem in tat_ca_diem:
        if diem < 0 or diem > 10:
            raise ValueError
#tinh diem trung binh ca nam cho tung mon
    t_cn = (t1 + t2 * 2) / 3
    v_cn = (v1 + v2 * 2) / 3
    a_cn = (a1 + a2 * 2) / 3
#tbmon * 0.9, cc * 0.1
    dtb_cac_mon = (t_cn + v_cn + a_cn) / 3
    dtb_tong = (dtb_cac_mon * 0.9) + (chuyen_can * 0.1)
#hien thi ket qua
    print("\n" + "=" * 40)
    print(f"Diem trung binh Toan ca nam: {t_cn:.2f}")
    print(f"Diem trung binh Van ca nam: {v_cn:.2f}")
    print(f"Diem trung binh Anh ca nam: {a_cn:.2f}")
    print("-" * 40)
    print(f"==> DIEM TONG KET CUOI NAM: {dtb_tong:.2f}")
    print("=" * 40)

    if dtb_tong >= 8.5:
        loai = "Gioi"
    elif dtb_tong >= 7.0:
        loai = "Kha"
    elif dtb_tong >= 5.0:
        loai = "Trung binh"
    else:
        loai = "Yeu"
    print(f"Xep loai: {loai}")
except ValueError:
    print("\n[LOI]: Vui long nhap so thuc hop le tu 0 den 10!")