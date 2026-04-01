import tkinter as tk
from tkinter import messagebox, ttk
import random

# --- DỮ LIỆU HỆ THỐNG ---
danh_sach_user = {"admin": "123456"}

# Thêm trường 'da_dung' để theo dõi hàng tiêu thụ trong tháng
kho_nguyen_lieu = {
    "Hạt Cà Phê Robusta": {"so_luong": random.randint(5, 50), "gia": 150000, "don_vi": "kg",
                           "da_dung": random.randint(10, 30)},
    "Sữa đặc Ngôi Sao": {"so_luong": random.randint(10, 30), "gia": 18000, "don_vi": "lon",
                         "da_dung": random.randint(20, 50)},
    "Sữa tươi Long Thành": {"so_luong": 5, "gia": 35000, "don_vi": "túi", "da_dung": random.randint(10, 40)},
    "Bột Matcha": {"so_luong": random.randint(1, 10), "gia": 450000, "don_vi": "kg", "da_dung": random.randint(2, 5)},
    "Đường cát": {"so_luong": random.randint(20, 100), "gia": 22000, "don_vi": "kg", "da_dung": random.randint(5, 15)},
    "Siro Đào": {"so_luong": 2, "gia": 120000, "don_vi": "chai", "da_dung": random.randint(3, 8)}
}


# --- GIAO DIỆN QUẢN LÝ KHO ---
def mo_giao_dien_kho(user_hien_tai):
    cua_so_login.withdraw()

    gui_kho = tk.Toplevel()
    gui_kho.title(f"Kho Cafe - Quản trị viên: {user_hien_tai}")
    gui_kho.geometry("800x650")
    gui_kho.configure(bg="#f4f7f6")

    gui_kho.protocol("WM_DELETE_WINDOW", lambda: cua_so_login.destroy())

    tk.Label(gui_kho, text=f"QUẢN TRỊ VIÊN: {user_hien_tai.upper()}", font=("Arial", 12, "bold"), fg="red",
             bg="#f4f7f6").pack(pady=5)
    tk.Label(gui_kho, text="HỆ THỐNG KHO & THỐNG KÊ CHI PHÍ", font=("Arial", 18, "bold"), bg="#f4f7f6").pack(pady=5)

    # Thanh tìm kiếm
    khung_tim = tk.Frame(gui_kho, bg="#f4f7f6")
    khung_tim.pack(fill="x", padx=20, pady=10)
    o_tim = tk.Entry(khung_tim, width=30)
    o_tim.pack(side="left", padx=5)

    # Bảng hiển thị
    khung_bang = tk.Frame(gui_kho)
    khung_bang.pack(padx=20)
    cot = ("ten", "sl", "dv", "gia", "used")
    bang_kho = ttk.Treeview(khung_bang, columns=cot, show="headings", height=12)
    bang_kho.heading("ten", text="Tên Nguyên Liệu")
    bang_kho.heading("sl", text="Tồn Kho")
    bang_kho.heading("dv", text="Đơn Vị")
    bang_kho.heading("gia", text="Giá Vốn")
    bang_kho.heading("used", text="Đã Dùng (Tháng)")

    bang_kho.column("sl", width=80)
    bang_kho.column("used", width=120)
    bang_kho.pack()

    def load_data(hien_thi=None):
        for i in bang_kho.get_children(): bang_kho.delete(i)
        data = hien_thi if hien_thi is not None else kho_nguyen_lieu
        for k, v in data.items():
            bang_kho.insert("", "end", values=(k, v["so_luong"], v["don_vi"], f"{v['gia']:,}", v["da_dung"]))

    def nut_tim():
        txt = o_tim.get().lower()
        kq = {k: v for k, v in kho_nguyen_lieu.items() if txt in k.lower()}
        load_data(kq)

    tk.Button(khung_tim, text="Tìm kiếm", command=nut_tim, bg="#3498db", fg="white").pack(side="left")

    # --- HÀM THỐNG KÊ KINH PHÍ ---
    def xem_thong_ke():
        win_tk = tk.Toplevel(gui_kho)
        win_tk.title("Báo cáo tài chính tháng này")
        win_tk.geometry("400x350")

        tong_von = 0
        for k, v in kho_nguyen_lieu.items():
            tong_von += v["da_dung"] * v["gia"]

        # Giả định doanh thu bán ra gấp 2.5 lần tiền vốn nguyên liệu
        doanh_thu = tong_von * 2.5
        loi_nhuan = doanh_thu - tong_von

        tk.Label(win_tk, text="BÁO CÁO KINH PHÍ TRONG THÁNG", font=("Arial", 13, "bold"), pady=20).pack()

        txt_von = f"Tổng tiền vốn đã chi: {tong_von:,.0f} VNĐ"
        tk.Label(win_tk, text=txt_von, fg="blue", font=("Arial", 11)).pack(pady=5)

        txt_dt = f"Doanh thu dự kiến: {doanh_thu:,.0f} VNĐ"
        tk.Label(win_tk, text=txt_dt, fg="green", font=("Arial", 11)).pack(pady=5)

        tk.Label(win_tk, text="--------------------------").pack()

        txt_loi = f"LỢI NHUẬN RÒNG: {loi_nhuan:,.0f} VNĐ"
        tk.Label(win_tk, text=txt_loi, fg="red", font=("Arial", 12, "bold")).pack(pady=10)

        tk.Button(win_tk, text="Đóng", command=win_tk.destroy, width=10).pack(pady=10)

    # --- Các nút chức năng chính ---
    khung_nut = tk.Frame(gui_kho, bg="#f4f7f6")
    khung_nut.pack(pady=20)

    def phan_phoi():
        chon = bang_kho.focus()
        if not chon: return messagebox.showwarning("Lỗi", "Chọn hàng để xuất!")
        ten = bang_kho.item(chon, 'values')[0]
        if kho_nguyen_lieu[ten]["so_luong"] > 0:
            kho_nguyen_lieu[ten]["so_luong"] -= 1
            kho_nguyen_lieu[ten]["da_dung"] += 1
            load_data()
        else:
            messagebox.showerror("Hết hàng", "Không còn hàng trong kho để xuất!")

    tk.Button(khung_nut, text="Xuất ra quầy (-1)", bg="#f39c12", fg="white", width=18, command=phan_phoi).grid(row=0,
                                                                                                               column=0,
                                                                                                               padx=5)
    tk.Button(khung_nut, text="Nhập kho (+10)", bg="#2ecc71", fg="white", width=18, command=lambda: (
        kho_nguyen_lieu.update({bang_kho.item(bang_kho.focus(), 'values')[0]: {
            **kho_nguyen_lieu[bang_kho.item(bang_kho.focus(), 'values')[0]],
            "so_luong": kho_nguyen_lieu[bang_kho.item(bang_kho.focus(), 'values')[0]][
                            "so_luong"] + 10}}) if bang_kho.focus() else None, load_data())).grid(row=0, column=1,
                                                                                                  padx=5)
    tk.Button(khung_nut, text="THỐNG KÊ CHI PHÍ", bg="#9b59b6", fg="white", width=18, font=("Arial", 9, "bold"),
              command=xem_thong_ke).grid(row=1, column=0, columnspan=2, pady=15)
    tk.Button(khung_nut, text="Xem tất cả", width=15, command=lambda: load_data()).grid(row=0, column=2, padx=5)

    load_data()


# --- GIAO DIỆN ĐĂNG NHẬP (Giữ nguyên từ code trước) ---
cua_so_login = tk.Tk()
cua_so_login.title("Đăng nhập")
cua_so_login.geometry("350x350")

tk.Label(cua_so_login, text="QUẢN LÝ CAFE", font=("Arial", 16, "bold")).pack(pady=15)
tk.Label(cua_so_login, text="Tên đăng nhập:").pack()
ent_user = tk.Entry(cua_so_login);
ent_user.pack(pady=5)
tk.Label(cua_so_login, text="Mật khẩu:").pack()
ent_pass = tk.Entry(cua_so_login, show="*");
ent_pass.pack(pady=5)


def logic_login():
    u, p = ent_user.get(), ent_pass.get()
    if u in danh_sach_user and danh_sach_user[u] == p:
        mo_giao_dien_kho(u)
    else:
        messagebox.showerror("Lỗi", "Sai tài khoản!")


def mo_dk():
    win_dk = tk.Toplevel(cua_so_login);
    win_dk.geometry("300x300")
    tk.Label(win_dk, text="Tên mới:").pack()
    e_u = tk.Entry(win_dk);
    e_u.pack()
    tk.Label(win_dk, text="Mật khẩu:").pack()
    e_p1 = tk.Entry(win_dk, show="*");
    e_p1.pack()
    tk.Label(win_dk, text="Xác nhận MK:").pack()
    e_p2 = tk.Entry(win_dk, show="*");
    e_p2.pack()

    def dk():
        if e_p1.get() == e_p2.get() and e_u.get():
            danh_sach_user[e_u.get()] = e_p1.get()
            messagebox.showinfo("Xong", "Đã tạo xong!")
            win_dk.destroy()
        else:
            messagebox.showerror("Lỗi", "Kiểm tra lại mật khẩu!")

    tk.Button(win_dk, text="Đăng ký", command=dk).pack(pady=10)


tk.Button(cua_so_login, text="Đăng nhập", width=20, bg="#3498db", fg="white", command=logic_login).pack(pady=15)
tk.Button(cua_so_login, text="Đăng ký tài khoản", command=mo_dk).pack()

cua_so_login.mainloop()