import tkinter as tk
from tkinter import messagebox, ttk
import os

# Cấu hình màu sắc
COLOR_BG = "#1a1a2e"  # Nền chính
COLOR_FRAME = "#26263e"  # Nền khung/bảng
COLOR_TEXT = "#ffffff"  # Chữ trắng
COLOR_BTN_LOGIN = "#4caf50"  # Xanh lá
COLOR_BTN_REG = "#2196f3"  # Xanh dương
COLOR_BTN_LOGOUT = "#f44336"  # Đỏ

FILE_NAME = "users.txt"


# ===== Xử lý dữ liệu =====
def save_user(username, password, email):
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(f"{username},{password},{email}\n")


def check_user(username, password):
    if not os.path.exists(FILE_NAME): return False
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 3 and parts[0] == username and parts[1] == password:
                return True
    return False


# ===== Giao diện QUẢN LÝ KHO  =====
def open_dashboard():
    root.withdraw()
    dash = tk.Toplevel()
    dash.title("Hệ Thống Quản Lý Sản Phẩm Tồn Kho")
    dash.geometry("850x600")
    dash.configure(bg=COLOR_BG)

    # Header tối
    header = tk.Frame(dash, bg=COLOR_FRAME, height=80)
    header.pack(fill="x", pady=(0, 10))
    tk.Label(header, text="DANH SÁCH SẢN PHẨM TRONG KHO", fg=COLOR_TEXT, bg=COLOR_FRAME,
             font=("Arial", 18, "bold")).pack(pady=20)

    # Khung chứa bảng
    table_frame = tk.Frame(dash, bg=COLOR_BG)
    table_frame.pack(fill="both", expand=True, padx=20)

    # Cấu hình Style cho Bảng
    style = ttk.Style()
    style.theme_use("clam")  # Dùng giao diện clam để dễ đổi màu
    style.configure("Treeview",
                    background=COLOR_FRAME,
                    foreground=COLOR_TEXT,
                    fieldbackground=COLOR_FRAME,
                    rowheight=30,
                    font=("Arial", 10))
    style.configure("Treeview.Heading",
                    background="#333352",
                    foreground=COLOR_TEXT,
                    font=("Arial", 11, "bold"))
    style.map("Treeview", background=[('selected', COLOR_BTN_REG)])

    # Tạo bảng
    columns = ("ma", "ten", "ton_kho", "tinh_trang")
    tree = ttk.Treeview(table_frame, columns=columns, show="headings")

    tree.heading("ma", text="Mã Sản Phẩm")
    tree.heading("ten", text="Tên Sản Phẩm")
    tree.heading("ton_kho", text="Số Lượng Tồn")
    tree.heading("tinh_trang", text="Tình Trạng")

    tree.column("ma", width=120, anchor="center")
    tree.column("ten", width=300, anchor="w")
    tree.column("ton_kho", width=120, anchor="center")
    tree.column("tinh_trang", width=150, anchor="center")

    # Danh sách sản phẩm
    products = [
        ("MAY001", "Máy pha Cafe Breville 870", "05 cái", "Còn hàng"),
        ("LY022", "Bộ 6 ly thủy tinh chịu nhiệt", "42 bộ", "Còn hàng"),
        ("TRA05", "Bột Matcha Uji Nhật Bản", "12 kg", "Sắp hết"),
        ("SIRO-01", "Siro Monin Vani (1L)", "25 chai", "Còn hàng"),
        ("MAY-XAY", "Máy xay hạt Nuova Simonelli", "02 cái", "Hàng mới về"),
        ("ONG-09", "Ống hút giấy (Thùng 500 cái)", "10 thùng", "Còn hàng")
    ]

    for p in products:
        tree.insert("", "end", values=p)

    tree.pack(fill="both", expand=True)

    # Nút Đăng xuất
    def logout():
        dash.destroy()
        root.deiconify()

    btn_logout = tk.Button(dash, text="Đăng xuất", bg=COLOR_BTN_LOGOUT, fg="white",
                           command=logout, font=("Arial", 10, "bold"),
                           padx=20, pady=8, relief="flat", cursor="hand2")
    btn_logout.pack(pady=20)


# ===== Giao diện ĐĂNG KÝ =====
def open_register():
    root.withdraw()
    reg = tk.Toplevel()
    reg.title("Register")
    reg.geometry("700x600")
    reg.configure(bg=COLOR_BG)

    frame = tk.Frame(reg, bg=COLOR_FRAME, padx=40, pady=30)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="REGISTER", fg=COLOR_TEXT, bg=COLOR_FRAME, font=("Arial", 22, "bold")).pack(pady=(0, 20))

    def create_input(label_text, show_char=""):
        tk.Label(frame, text=label_text, fg=COLOR_TEXT, bg=COLOR_FRAME, font=("Arial", 11)).pack(anchor="w")
        entry = tk.Entry(frame, font=("Arial", 12), width=25, bg="white")
        if show_char: entry.config(show=show_char)
        entry.pack(pady=(5, 15))
        return entry

    e_user = create_input("Username")
    e_email = create_input("Email")
    e_pass = create_input("Password", "*")
    e_repass = create_input("Nhập lại mật khẩu", "*")

    def handle_reg():
        if e_pass.get() != e_repass.get():
            messagebox.showerror("Lỗi", "Mật khẩu không khớp!")
        elif not e_user.get():
            messagebox.showerror("Lỗi", "Vui lòng điền thông tin!")
        else:
            save_user(e_user.get(), e_pass.get(), e_email.get())
            messagebox.showinfo("OK", "Tạo tài khoản thành công!")
            reg.destroy()
            root.deiconify()

    tk.Button(frame, text="Đăng ký", bg=COLOR_BTN_REG, fg="white", font=("Arial", 12, "bold"),
              width=20, command=handle_reg, cursor="hand2").pack(pady=10)


# ===== Giao diện ĐĂNG NHẬP  =====
root = tk.Tk()
root.title("Login System")
root.geometry("700x600")
root.configure(bg=COLOR_BG)

login_frame = tk.Frame(root, bg=COLOR_FRAME, padx=50, pady=40)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(login_frame, text="LOGIN", fg=COLOR_TEXT, bg=COLOR_FRAME, font=("Arial", 22, "bold")).pack(pady=(0, 20))

tk.Label(login_frame, text="Username", fg=COLOR_TEXT, bg=COLOR_FRAME, font=("Arial", 11)).pack(anchor="w")
entry_username = tk.Entry(login_frame, font=("Arial", 12), width=25)
entry_username.pack(pady=(5, 15))

tk.Label(login_frame, text="Password", fg=COLOR_TEXT, bg=COLOR_FRAME, font=("Arial", 11)).pack(anchor="w")
entry_password = tk.Entry(login_frame, font=("Arial", 12), width=25, show="*")
entry_password.pack(pady=(5, 20))


def login():
    if check_user(entry_username.get(), entry_password.get()):
        open_dashboard()
    else:
        messagebox.showerror("Lỗi", "Sai tài khoản hoặc mật khẩu!")


tk.Button(login_frame, text="Đăng nhập", bg=COLOR_BTN_LOGIN, fg="white",
          font=("Arial", 12, "bold"), width=20, command=login, cursor="hand2").pack(pady=5)

tk.Button(login_frame, text="Tạo tài khoản", bg=COLOR_BTN_REG, fg="white",
          font=("Arial", 12, "bold"), width=20, command=open_register, cursor="hand2").pack(pady=5)

root.mainloop()