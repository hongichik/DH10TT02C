import tkinter as tk

tai_khoan = {}

def dang_ky():
    user = entry_user.get()
    password = entry_pass.get()

    if user in tai_khoan:
        print("Tài khoản đã tồn tại!")
    else:
        tai_khoan[user] = password
        print("Tạo tài khoản thành công!")


def dang_nhap():
    user = entry_user.get()
    password = entry_pass.get()

    if user in tai_khoan and tai_khoan[user] == password:
        print("Đăng nhập thành công!")
    else:
        print("Sai tài khoản hoặc mật khẩu!")



root = tk.Tk()
root.title("Trang đăng nhập")
root.geometry("300x300")
root.configure(bg="lightblue")


tk.Label(root, text="TRƯỜNG ĐẠI HỌC HẠ LONG",
         font=("Arial", 14, "bold"),
         bg="lightblue").pack(pady=10)


tk.Label(root, text="Tài khoản", bg="lightblue").pack()
entry_user = tk.Entry(root)
entry_user.pack()


tk.Label(root, text="Mật Khẩu", bg="lightblue").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()


tk.Button(root, text="Đăng nhập", command=dang_nhap).pack(pady=5)


tk.Button(root, text="Tạo Tài Khoản", command=dang_ky).pack(pady=5)

root.mainloop()