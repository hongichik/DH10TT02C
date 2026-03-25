# Tạo dictionary chứa thông tin cá nhân
person = {
    "ten": "An",
    "tuoi": 20,
    "nghe_nghiep": "Sinh vien"
}
print("Ban đầu:", person)

# Thêm thông tin email
person["email"] = "an@gmail.com"
print("Sau khi thêm email:", person)

# Sửa tuổi thành 25
person["tuoi"] = 25
print("Sau khi sửa tuổi:", person)

# Xóa thông tin nghề nghiệp
del person["nghe_nghiep"]
print("Dictionary cuối:", person)