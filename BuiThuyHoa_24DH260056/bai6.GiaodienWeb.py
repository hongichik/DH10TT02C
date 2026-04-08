import tkinter as tk
from tkinter import messagebox, font

# --- ĐỊNH NGHĨA MÀU SẮC ---
MAU_NEN = "#FDF0F6"  # Hồng Pastel rất nhẹ
MAU_NHAT = "#FCE4EC"  # Hồng nhạt hơn cho khung
MAU_TIM_DAM = "#6A1B9A"  # Tím đậm vừa cho tiêu đề và chữ quan trọng
MAU_TIM_NUT = "#AB47BC"  # Tím trung bình cho nút bấm


class RegisterUI:

    def __init__(self, parent_window):
        self.window = tk.Toplevel(parent_window)
        self.parent = parent_window
        self.parent.withdraw()  # Ẩn cửa sổ Đăng nhập

        self.window.title("Thành viên mới - Đăng ký")
        self.window.geometry("400x550")
        self.window.configure(bg=MAU_NEN)

        # Khi đóng cửa sổ đăng ký bằng dấu "X", hiện lại cửa sổ login
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        self.setup_ui()

    def setup_ui(self):
        # Container chính
        self.main_container = tk.Frame(self.window, bg=MAU_NEN)
        self.main_container.place(relx=0.5, rely=0.5, anchor="center")

        # Tiêu đề
        tk.Label(
            self.main_container, text="TẠO TÀI KHOẢN",
            font=("Helvetica", 18, "bold"), bg=MAU_NEN, fg=MAU_TIM_DAM
        ).pack(pady=(0, 25))

        # Các trường nhập liệu
        self.create_input_field("Tên đăng nhập:", "user")
        self.create_input_field("Email:", "email")
        self.create_input_field("Mật khẩu:", "pass", is_password=True)
        self.create_input_field("Xác nhận mật khẩu:", "confirm", is_password=True)

        # Nút Đăng ký
        tk.Button(
            self.main_container, text="HOÀN TẤT ✨", command=self.validate_registration,
            bg=MAU_TIM_DAM, fg="white", font=("Helvetica", 10, "bold"),
            padx=20, pady=8, cursor="hand2", bd=0, width=18
        ).pack(pady=20)

        # Link quay lại
        back_btn = tk.Label(
            self.main_container, text="Đã có tài khoản? Quay lại",
            bg=MAU_NEN, fg=MAU_TIM_NUT, cursor="hand2", font=("Helvetica", 9, "underline")
        )
        back_btn.pack()
        back_btn.bind("<Button-1>", lambda e: self.on_close())

    def create_input_field(self, label_text, attr_name, is_password=False):
        frame = tk.Frame(self.main_container, bg=MAU_NEN)
        frame.pack(fill="x", pady=5)

        tk.Label(frame, text=label_text, font=("Arial", 10), bg=MAU_NEN, fg=MAU_TIM_DAM, anchor="w").pack(fill="x")

        entry = tk.Entry(
            frame, font=("Arial", 11), show="*" if is_password else "",
            bd=0, highlightthickness=1, highlightbackground=MAU_TIM_NUT
        )
        entry.pack(fill="x", ipady=4, pady=(2, 8))
        setattr(self, f"{attr_name}_entry", entry)

    def validate_registration(self):

        u = self.user_entry.get()
        if not u:
            messagebox.showwarning("Nhắc nhở", "Vui lòng điền đủ thông tin nhé! ✨")
            return
        messagebox.showinfo("Thành công", f"Chào mừng {u}!\nTài khoản đã sẵn sàng.")
        self.on_close()

    def on_close(self):
        self.window.destroy()
        self.parent.deiconify()


# --- GIAO DIỆN ĐĂNG NHẬP CHÍNH ---

def mo_dang_ky():
    RegisterUI(root)


def login():
    u = entry_username.get()
    if u:
        messagebox.showinfo("Chào mừng", f"Hí chào {u} nhé! ✨")
    else:
        messagebox.showwarning("Lỗi", "Nhập tên đăng nhập đã nè!")


root = tk.Tk()
root.title("Đăng nhập")
root.geometry("350x400")
root.configure(bg=MAU_NEN)

# Header trang trí
tk.Label(root, text="Đăng Nhập", font=("Helvetica", 22, "bold"), bg=MAU_NEN, fg=MAU_TIM_DAM).pack(pady=(40, 20))

# Khung nhập liệu Login
frame_login = tk.Frame(root, bg=MAU_NEN)
frame_login.pack(pady=10, padx=40, fill="x")

tk.Label(frame_login, text="Tên đăng nhập:", bg=MAU_NEN, fg=MAU_TIM_DAM).pack(anchor="w")
entry_username = tk.Entry(frame_login, bd=0, highlightthickness=1, highlightbackground=MAU_TIM_NUT)
entry_username.pack(fill="x", ipady=5, pady=(5, 15))

tk.Label(frame_login, text="Mật khẩu:", bg=MAU_NEN, fg=MAU_TIM_DAM).pack(anchor="w")
entry_password = tk.Entry(frame_login, show="*", bd=0, highlightthickness=1, highlightbackground=MAU_TIM_NUT)
entry_password.pack(fill="x", ipady=5, pady=(5, 15))

# Nút bấm Login
tk.Button(
    root, text="ĐĂNG NHẬP", command=login,
    bg=MAU_TIM_DAM, fg="white", font=("Arial", 10, "bold"),
    bd=0, width=15, cursor="hand2"
).pack(pady=10, ipady=5)

# Nút chuyển sang Đăng ký
tk.Button(
    root, text="Tạo tài khoản mới", command=mo_dang_ky,
    bg=MAU_NEN, fg=MAU_TIM_NUT, bd=0, font=("Arial", 9, "underline"), cursor="hand2"
).pack()

root.mainloop()