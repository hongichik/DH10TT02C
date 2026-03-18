ca_nhan = {
    "ten": "Viet Anh",
    "tuoi": 20,
    "nghe_nghiep": "Sinh vien",
}

print(ca_nhan)

ca_nhan["email"] = "phamvietanh10a2hd@gmail.com"

print(ca_nhan)

ca_nhan["tuoi"] = 25
print(ca_nhan)

ca_nhan.pop("nghe_nghiep")
print(ca_nhan)