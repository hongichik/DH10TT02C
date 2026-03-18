ca_nhan = {
    "ten": "Long",
    "tuoi": 20,
    "nghe_nghiep": "Sinh viên",
}

print(ca_nhan)

ca_nhan["email"] = "Nhatlonghl2512@gmail.com"

print(ca_nhan)

ca_nhan["tuoi"] = 25
print(ca_nhan)

ca_nhan.pop("nghe_nghiep")
print(ca_nhan)