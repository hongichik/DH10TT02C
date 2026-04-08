import tkinter as tk
from tkinter import messagebox

# --- CẤU HÌNH GIAO DIỆN CAFE ---
COLOR_DARK_COFFEE = "#3D2B1F"
COLOR_BROWN = "#6F4E37"
COLOR_CREAM = "#FDF5E6"
COLOR_WHITE = "#FFFFFF"


class CoffeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ Thống Quản Lý Cafe - Login")
        self.root.geometry("400x600")
        self.root.configure(bg=COLOR_WHITE)

        # Cơ sở dữ liệu tạm thời
        self.users = {"admin": "123456"}

        # Chạy giao diện đăng nhập đầu tiên
        self.setup_login_ui()

    def clear_window(self):
        """Xóa sạch các widget cũ để vẽ giao diện mới"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_input_group(self, label_text, attr_name, is_password=False):
        """Hàm hỗ trợ tạo nhãn và ô nhập liệu nhanh"""
        frame = tk.Frame(self.root, bg=COLOR_WHITE)
        frame.pack(fill="x", padx=50, pady=5)

        tk.Label(frame, text=label_text, bg=COLOR_WHITE, fg=COLOR_BROWN, font=("Arial", 10, "bold")).pack(anchor="w")

        entry = tk.Entry(
            frame, font=("Arial", 11), bg="#F8F9FA", bd=0,
            highlightthickness=1, highlightbackground="#DCDDE1",
            show="*" if is_password else ""
        )
        entry.pack(fill="x", ipady=8, pady=(5, 10))
        setattr(self, attr_name, entry)

    def setup_login_ui(self):
        self.clear_window()

        # Logo và Tiêu đề
        tk.Label(self.root, text="☕", font=("Arial", 60), bg=COLOR_WHITE, fg=COLOR_BROWN).pack(pady=(40, 10))
        tk.Label(self.root, text="ĐĂNG NHẬP", font=("Arial", 18, "bold"), bg=COLOR_WHITE, fg=COLOR_DARK_COFFEE).pack(
            pady=(0, 30))

        # Nhập liệu
        self.create_input_group("Tên đăng nhập:", "ent_u_login")
        self.create_input_group("Mật khẩu:", "ent_p_login", is_password=True)

        # Nút Đăng nhập
        btn_login = tk.Button(
            self.root, text="ĐĂNG NHẬP", command=self.handle_login,
            bg=COLOR_BROWN, fg=COLOR_WHITE, font=("Arial", 11, "bold"),
            bd=0, cursor="hand2", width=25
        )
        btn_login.pack(pady=20, ipady=10)

        # Chuyển sang Đăng ký
        tk.Button(
            self.root, text="Chưa có tài khoản? Đăng ký ngay", command=self.setup_register_ui,
            fg="#2980B9", bg=COLOR_WHITE, bd=0, font=("Arial", 9, "underline"), cursor="hand2"
        ).pack()

    def setup_register_ui(self):
        self.clear_window()

        tk.Label(self.root, text="TẠO TÀI KHOẢN", font=("Arial", 18, "bold"), bg=COLOR_WHITE, fg=COLOR_BROWN).pack(
            pady=40)

        # Form đăng ký (Đầy đủ các trường từ code của bạn)
        self.create_input_group("Tên đăng nhập:", "reg_u")
        self.create_input_group("Email:", "reg_e")
        self.create_input_group("Mật khẩu:", "reg_p")
        self.create_input_group("Xác nhận mật khẩu:", "reg_c", is_password=True)

        # Nút Xác nhận
        btn_reg = tk.Button(
            self.root, text="XÁC NHẬN ĐĂNG KÝ", command=self.handle_register,
            bg="#27AE60", fg=COLOR_WHITE, font=("Arial", 11, "bold"),
            bd=0, cursor="hand2", width=25
        )
        btn_reg.pack(pady=25, ipady=10)

        # Quay lại Đăng nhập
        tk.Button(
            self.root, text="Đã có tài khoản? Quay lại đăng nhập", command=self.setup_login_ui,
            fg="#2980B9", bg=COLOR_WHITE, bd=0, font=("Arial", 9, "underline"), cursor="hand2"
        ).pack()

    def handle_login(self):
        u = self.ent_u_login.get()
        p = self.ent_p_login.get()
        if u in self.users and self.users[u] == p:
            messagebox.showinfo("Thành công", f"Chào mừng {u}!")
        else:
            messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu!")

    def handle_register(self):
        u, e, p, c = self.reg_u.get(), self.reg_e.get(), self.reg_p.get(), self.reg_c.get()

        if not all([u, e, p, c]):
            messagebox.showwarning("Chú ý", "Bạn cần điền đủ thông tin!")
            return
        if p != c:
            messagebox.showerror("Lỗi", "Mật khẩu không khớp!")
            return

        self.users[u] = p
        messagebox.showinfo("Hoàn tất", f"Chúc mừng {u} đã đăng ký thành công!")
        self.setup_login_ui()


if __name__ == "__main__":
    app_root = tk.Tk()
    app = CoffeeApp(app_root)
    app_root.mainloop()