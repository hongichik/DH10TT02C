ca_nhan = {
    "ten": "Dang Khoa",
    "tuoi": 20,
    "nghe_nghiep": "Sinh vien",
}

print(ca_nhan)

ca_nhan["email"] = "mdk28072006@gmail.com"

print(ca_nhan)

ca_nhan["tuoi"] = 25
print(ca_nhan)

ca_nhan.pop("nghe_nghiep")
print(ca_nhan)