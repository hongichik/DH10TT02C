import tkinter as tk
from tkinter import messagebox


# Create main window
root = tk.Tk()
root.title("Login")
root.geometry("300x200")

# Add a label
label = tk.Label(root, text="Đăng nhập", font=("Arial", 20))
label.pack(pady=10)
lib_user = tk.Label(root, text="Username:")
lib_user.place(x=20, y=60)

lib_pass = tk.Label(root, text="Password:")
lib_pass.place(x=20, y=100)

entry_username = tk.Entry(root)
entry_username.place(x=90, y=60)

entry_password = tk.Entry(root, show="*")
entry_password.place(x=90, y=100)

def login():
    messagebox.showinfo("Login Info", f"Username: {entry_username.get()}\nPassword: {entry_password.get()}")
def tao_tk():
    root.destroy()
    taotk.show()
btn = tk.Button(root, text="Tạo tài khoản", command=tao_tk)
btn.place(x=40, y=140)

btn = tk.Button(root, text="Đăng nhập", command=login)
btn.place(x=160, y=140)

root.mainloop()
import tkinter as tk
from tkinter import messagebox, font


class RegisterUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống - Tạo tài khoản")
        self.root.geometry("450x500")
        self.root.configure(bg="#f4f4f9")  # Màu nền xám nhạt hiện đại

        # Thiết lập font chữ
        self.title_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.label_font = font.Font(family="Helvetica", size=10)
        self.entry_font = font.Font(family="Helvetica", size=11)

        self.setup_ui()

    def setup_ui(self):
        # Khung chứa chính để căn giữa
        self.main_container = tk.Frame(self.root, bg="#f4f4f9")
        self.main_container.place(relx=0.5, rely=0.5, anchor="center")

        # --- Tiêu đề ---
        tk.Label(
            self.main_container,
            text="ĐĂNG KÝ",
            font=self.title_font,
            bg="#f4f4f9",
            fg="#333333"
        ).pack(pady=(0, 30))

        # --- Các trường nhập liệu ---
        self.create_input_field("Tên đăng nhập:", "user")
        self.create_input_field("Email:", "email")
        self.create_input_field("Mật khẩu:", "pass", is_password=True)
        self.create_input_field("Xác nhận mật khẩu:", "confirm", is_password=True)

        # --- Nút Đăng ký ---
        self.reg_btn = tk.Button(
            self.main_container,
            text="TẠO TÀI KHOẢN",
            command=self.validate_registration,
            bg="#4CAF50",  # Màu xanh lá
            fg="white",
            font=("Helvetica", 10, "bold"),
            padx=20,
            pady=10,
            cursor="hand2",
            bd=0,
            width=20
        )
        self.reg_btn.pack(pady=20)

        # --- Link quay lại ---
        self.back_link = tk.Label(
            self.main_container,
            text="Đã có tài khoản? Đăng nhập ngay",
            bg="#f4f4f9",
            fg="#007bff",
            cursor="hand2",
            font=("Helvetica", 9, "underline")
        )
        self.back_link.pack()

    def create_input_field(self, label_text, attr_name, is_password=False):
        """Hàm hỗ trợ tạo nhanh các dòng nhập liệu"""
        frame = tk.Frame(self.main_container, bg="#f4f4f9")
        frame.pack(fill="x", pady=5)

        tk.Label(frame, text=label_text, font=self.label_font, bg="#f4f4f9", anchor="w").pack(fill="x")

        entry = tk.Entry(
            frame,
            font=self.entry_font,
            show="*" if is_password else "",
            bd=1,
            relief="solid"
        )
        entry.pack(fill="x", ipady=5, pady=(2, 10))

        # Lưu biến entry vào object để truy xuất sau này
        setattr(self, f"{attr_name}_entry", entry)

    def validate_registration(self):
        """Hàm xử lý logic khi nhấn nút"""
        u = self.user_entry.get()
        e = self.email_entry.get()
        p = self.pass_entry.get()
        c = self.confirm_entry.get()

        if not all([u, e, p, c]):
            messagebox.showwarning("Thông báo", "Vui lòng điền đầy đủ thông tin!")
            return

        if p != c:
            messagebox.showerror("Lỗi", "Mật khẩu xác nhận không khớp!")
            return

        messagebox.showinfo("Thành công", f"Chào mừng {u}!\nTài khoản đã được khởi tạo.")


def show():
    app = tk.Tk()
    ui = RegisterUI(app)
    app.mainloop()