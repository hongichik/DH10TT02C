import tkinter as tk
from page.login import LoginPage
from page.quanlyhs import QuanLyHSPage
from page.themhs import ThemHSPage
from page.suahs import SuaHSPage


class AppManager:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quản lý học sinh - Tiểu học Quang Trung")
        self.root.geometry("300x200")
        self.current_page = None
        self.show_login_page()

    "Xóa tất cả widget của page hiện tại"
    def clear_current_page(self):
        if self.current_page:
            for widget in self.root.winfo_children():
                widget.destroy()

    "Hiển thị trang đăng nhập"
    def show_login_page(self):
        self.clear_current_page()
        self.root.geometry("300x200")
        self.current_page = LoginPage(self.root, self)

    "Hiển thị trang QL hs"
    def show_quanlyhs_page(self):
        self.clear_current_page()
        self.root.geometry("600x400")
        self.current_page = QuanLyHSPage(self.root, self)

    "Hiển thị trang thêm thông tin hs"
    def show_themhs_page(self):
        self.clear_current_page()
        self.root.geometry("400x300")
        self.current_page = ThemHSPage(self.root, self)

    "Hiển thị trang sửa thông tin hs"
    def show_suahs_page(self, index):
        self.clear_current_page()
        self.root.geometry("400x300")
        self.current_page = SuaHSPage(self.root, self, index)

    "chạy ứng dụng"
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = AppManager()
    app.run()