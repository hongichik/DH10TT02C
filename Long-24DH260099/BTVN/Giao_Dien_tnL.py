import tkinter as tk
from tkinter import messagebox, ttk
import random
import platform
from datetime import datetime

# --- DỮ LIỆU HỆ THỐNG ---
danh_sach_user = {"admin": "123456"}
lich_su_truy_cap = []  # Lưu: Tài khoản, Thiết bị, Thời gian
mau_ngau_nhien = ["#fff5e6", "#f2ffe6", "#e6f7ff", "#f9e6ff", "#ffe6e6", "#e6fff2"]

kho_nguyen_lieu = {
    "Hạt Cà Phê Robusta": {"so_luong": random.randint(5, 50), "gia": 150, "dv": "kg", "dung": random.randint(10, 30)},
    "Sữa đặc Ngôi Sao": {"so_luong": random.randint(10, 30), "gia": 18, "dv": "lon", "dung": random.randint(20, 50)},
    "Sữa tươi Long Thành": {"so_luong": 15, "gia": 35, "dv": "túi", "dung": random.randint(10, 40)},
    "Bột Matcha Nhật": {"so_luong": random.randint(1, 10), "gia": 450, "dv": "kg", "dung": random.randint(2, 5)},
    "Đường cát trắng": {"so_luong": random.randint(20, 100), "gia": 22, "dv": "kg", "dung": random.randint(5, 15)},
    "Siro Đào Pháp": {"so_luong": 12, "gia": 120, "dv": "chai", "dung": random.randint(3, 8)}
}


# --- GIAO DIỆN LỊCH SỬ ĐĂNG NHẬP ---
def xem_lich_su():
    win_ls = tk.Toplevel()
    win_ls.title("Nhật ký truy cập")
    win_ls.geometry("550x400")
    win_ls.configure(bg="white")

    # Header đồng bộ màu Nâu Coffee
    header_ls = tk.Frame(win_ls, bg="#6f4e37", height=60)
    header_ls.pack(fill="x")
    tk.Label(header_ls, text="LỊCH SỬ ĐĂNG NHẬP HỆ THỐNG", font=("Arial", 12, "bold"), bg="#6f4e37", fg="white").pack(
        pady=15)

    frame = tk.Frame(win_ls, bg="white")
    frame.pack(padx=15, pady=10, fill="both", expand=True)

    cols = ("user", "device", "time")
    tree = ttk.Treeview(frame, columns=cols, show="headings")
    tree.heading("user", text="Tài khoản")
    tree.heading("device", text="Tên thiết bị")
    tree.heading("time", text="Thời gian đăng nhập")

    tree.column("user", width=100)
    tree.column("device", width=150)
    tree.column("time", width=200)
    tree.pack(fill="both", expand=True)

    for log in lich_su_truy_cap:
        tree.insert("", "end", values=log)


# --- GIAO DIỆN CHÍNH (KHO HÀNG) ---
def mo_giao_dien_kho(user_name):
    root.withdraw()  # Ẩn màn hình đăng nhập
    gui_kho = tk.Toplevel()
    gui_kho.title(f"Quản Lý Kho - Xin chào {user_name}")
    gui_kho.geometry("900x750")
    gui_kho.configure(bg="#ffffff")

    # Đăng xuất: Đóng kho, hiện lại Login
    def dang_xuat():
        if messagebox.askyesno("Đăng xuất", "Bạn có chắc muốn quay lại màn hình đăng nhập?"):
            gui_kho.destroy()
            root.deiconify()

    gui_kho.protocol("WM_DELETE_WINDOW", lambda: root.destroy())

    # Header màu Nâu Coffee chủ đạo
    header = tk.Frame(gui_kho, bg="#6f4e37", height=80)
    header.pack(fill="x")
    tk.Label(header, text="☕ HỆ THỐNG QUẢN LÝ KHO", font=("Arial", 18, "bold"), fg="white", bg="#6f4e37").pack(pady=15)

    # Thanh điều hướng (Đăng xuất & Lịch sử)
    nav = tk.Frame(gui_kho, bg="#f8f9fa")
    nav.pack(fill="x")
    tk.Button(nav, text="Đăng xuất", command=dang_xuat, fg="#e74c3c", bg="#f8f9fa", font=("Arial", 9, "bold"),
              bd=0).pack(side="right", padx=20, pady=10)
    tk.Button(nav, text="Lịch sử đăng nhập", command=xem_lich_su, fg="#2980b9", bg="#f8f9fa", font=("Arial", 9),
              bd=0).pack(side="right", padx=10)
    tk.Label(nav, text=f"Admin: {user_name}", bg="#f8f9fa", fg="#7f8c8d").pack(side="left", padx=20)

    # Bảng dữ liệu
    frame_table = tk.Frame(gui_kho, bg="white")
    frame_table.pack(pady=10, padx=20, fill="both", expand=True)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", rowheight=30)
    style.configure("Treeview.Heading", background="#f1f3f4", font=("Arial", 10, "bold"))

    cols = ("ten", "sl", "dv", "gia", "da_dung")
    bang = ttk.Treeview(frame_table, columns=cols, show="headings")
    bang.heading("ten", text="Tên Nguyên Liệu")
    bang.heading("sl", text="Tồn Kho")
    bang.heading("dv", text="Đơn Vị")
    bang.heading("gia", text="Giá Nhập (.000đ)")
    bang.heading("da_dung", text="Tiêu Thụ")
    bang.pack(fill="both", expand=True)

    def load_data():
        for i in bang.get_children(): bang.delete(i)
        for k, v in kho_nguyen_lieu.items():
            color = random.choice(mau_ngau_nhien)
            tag_name = f"tag_{k}"
            bang.tag_configure(tag_name, background=color)
            bang.insert("", "end", values=(k, v["so_luong"], v["dv"], f"{v['gia']:,}", v["dung"]), tags=(tag_name,))

    # --- HÀM XEM CHI TIẾT (Đã được tô màu đồng bộ) ---
    def on_double_click(event):
        try:
            item = bang.selection()[0]
            ten = bang.item(item, "values")[0]
            data = kho_nguyen_lieu[ten]

            win_info = tk.Toplevel(gui_kho)
            win_info.geometry("350x280")
            win_info.title(f"Chi tiết: {ten}")
            win_info.configure(bg="white")

            # Header cửa sổ chi tiết màu Nâu Coffee
            header_info = tk.Frame(win_info, bg="#6f4e37", height=50)
            header_info.pack(fill="x")
            tk.Label(header_info, text=f"THÔNG TIN: {ten.upper()}", font=("Arial", 11, "bold"), bg="#6f4e37",
                     fg="white").pack(pady=12)

            # Nội dung chi tiết trên nền trắng/kem đồng bộ
            tk.Label(win_info, text=f"Đơn vị tính: {data['dv']}", font=("Arial", 10), bg="white").pack(pady=(15, 5))
            tk.Label(win_info, text=f"Số lượng tồn hiện tại: {data['so_luong']}", font=("Arial", 10), bg="white").pack(
                pady=5)
            tk.Label(win_info, text=f"Đã tiêu thụ tháng này: {data['dung']}", font=("Arial", 10), bg="white").pack(
                pady=5)

            # Phần chi phí nổi bật
            frame_cost = tk.Frame(win_info, bg="#fff8f0", bd=1, relief="solid")  # Màu nền hơi kem
            frame_cost.pack(pady=15, padx=20, fill="x")
            tk.Label(frame_cost, text=f"Tổng chi phí vốn (Tháng):", font=("Arial", 10, "bold"), bg="#fff8f0",
                     fg="#6f4e37").pack(pady=(5, 0))
            tk.Label(frame_cost, text=f"{data['dung'] * data['gia']:,.0f}.000đ", font=("Arial", 14, "bold"),
                     bg="#fff8f0", fg="blue").pack(pady=(0, 5))

        except:
            pass

    bang.bind("<Double-1>", on_double_click)

    # Nút bấm kho
    frame_btn = tk.Frame(gui_kho, bg="white")
    frame_btn.pack(pady=20)

    def action_nhap():
        sel = bang.focus()
        if sel:
            ten = bang.item(sel, 'values')[0]
            kho_nguyen_lieu[ten]["so_luong"] += 10
            load_data()

    tk.Button(frame_btn, text="NHẬP KHO (+10)", bg="#27ae60", fg="white", width=18, command=action_nhap).pack(
        side="left", padx=10, ipady=5)
    tk.Button(frame_btn, text="TẢI LẠI BẢNG", bg="#6f4e37", fg="white", width=18, command=load_data).pack(side="left",
                                                                                                          padx=10,
                                                                                                          ipady=5)

    load_data()


# --- GIAO DIỆN LOGIN (Giữ nguyên) ---
root = tk.Tk()
root.title("Coffee Login")
root.geometry("400x550")
root.configure(bg="white")

tk.Label(root, text="☕", font=("Arial", 50), bg="white", fg="#6f4e37").pack(pady=(30, 0))
tk.Label(root, text="ĐĂNG NHẬP QUẢN TRỊ", font=("Arial", 14, "bold"), bg="white", fg="#3d2b1f").pack(pady=(0, 20))


def make_entry(txt, hide=False):
    tk.Label(root, text=txt, bg="white", fg="#7f8c8d").pack(anchor="w", padx=50)
    e = tk.Entry(root, font=("Arial", 11), bg="#f8f9fa", bd=0, highlightthickness=1, highlightbackground="#dcdde1")
    if hide: e.config(show="*")
    e.pack(fill="x", padx=50, pady=(5, 15), ipady=8)
    return e


ent_u = make_entry("Tài khoản")
ent_p = make_entry("Mật khẩu", True)


def handle_login():
    u, p = ent_u.get(), ent_p.get()
    if u in danh_sach_user and danh_sach_user[u] == p:
        thiet_bi = platform.node()
        gio = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
        lich_su_truy_cap.append((u, thiet_bi, gio))

        mo_giao_dien_kho(u)
        ent_u.delete(0, tk.END)
        ent_p.delete(0, tk.END)
    else:
        messagebox.showerror("Lỗi", "Tài khoản hoặc mật khẩu không chính xác!")


def handle_register():
    win_reg = tk.Toplevel(root)
    win_reg.title("Đăng ký tài khoản")
    win_reg.geometry("350x400")
    win_reg.configure(bg="white")

    # Header đăng ký cũng đồng bộ màu Nâu Coffee
    header_reg = tk.Frame(win_reg, bg="#6f4e37", height=50)
    header_reg.pack(fill="x")
    tk.Label(header_reg, text="ĐĂNG KÝ MỚI", font=("Arial", 12, "bold"), bg="#6f4e37", fg="white").pack(pady=12)

    # tk.Label(win_reg, text="ĐĂNG KÝ MỚI", font=("Arial", 12, "bold"), bg="white").pack(pady=20) # Bỏ Label cũ

    tk.Label(win_reg, text="Tên đăng nhập:", bg="white").pack(pady=(15, 0))
    r_u = tk.Entry(win_reg, bg="#f1f3f4", bd=0);
    r_u.pack(pady=5, ipady=5, padx=40, fill="x")

    tk.Label(win_reg, text="Mật khẩu:", bg="white").pack()
    r_p1 = tk.Entry(win_reg, show="*", bg="#f1f3f4", bd=0);
    r_p1.pack(pady=5, ipady=5, padx=40, fill="x")

    tk.Label(win_reg, text="Nhập lại mật khẩu:", bg="white").pack()
    r_p2 = tk.Entry(win_reg, show="*", bg="#f1f3f4", bd=0);
    r_p2.pack(pady=5, ipady=5, padx=40, fill="x")

    def save():
        if r_p1.get() != r_p2.get():
            messagebox.showerror("Lỗi", "Mật khẩu không khớp!")
        elif not r_u.get() or not r_p1.get():
            messagebox.showwarning("!", "Vui lòng nhập đầy đủ thông tin!")
        else:
            danh_sach_user[r_u.get()] = r_p1.get()
            messagebox.showinfo("Xong", "Đã tạo tài khoản thành công!")
            win_reg.destroy()

    tk.Button(win_reg, text="XÁC NHẬN ĐĂNG KÝ", bg="#6f4e37", fg="white", font=("Arial", 10, "bold"),
              command=save).pack(pady=25, ipady=8, padx=40, fill="x")


# Nút chính màn hình Login
tk.Button(root, text="ĐĂNG NHẬP", bg="#6f4e37", fg="white", font=("Arial", 11, "bold"), command=handle_login,
          bd=0).pack(fill="x", padx=50, pady=15, ipady=10)
tk.Button(root, text="Tạo tài khoản quản trị mới", fg="#2980b9", bg="white", bd=0, command=handle_register).pack()

root.mainloop()