ca_nhan = {
    "ten": "Duy Tien",
    "tuoi": 20,
    "nghe_nghiep": "Sinh Vien",
}
print(ca_nhan)
ca_nhan["email"] = "duytien@daihochalong.edu.vn"
print(ca_nhan)
ca_nhan["tuoi"] = 25
print(ca_nhan)
ca_nhan.pop("nghe_nghiep")
print(ca_nhan)