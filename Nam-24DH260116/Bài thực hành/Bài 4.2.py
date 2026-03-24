ca_nhan = {
    "ten":"nam le",
    "tuoi":"20",
    "nghe_nghiep":"Sinh vien",
}
print(ca_nhan)
ca_nhan["email"] = "namdepzai@gmail.com"
print(ca_nhan)
ca_nhan["tuoi"] = 25
print(ca_nhan)
ca_nhan.pop("nghe_nghiep")
print(ca_nhan)