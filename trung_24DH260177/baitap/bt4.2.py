ca_nhan={
    "ten": "Van Lam",
    "tuoi":20,
    "nghe_nghiep": "Tự do",
}
print(ca_nhan)
ca_nhan["email"]= "vuvanlam1811@gmail.com"
print(ca_nhan)
ca_nhan["tuoi"]= 19
print(ca_nhan)
ca_nhan.pop("nghe_nghiep")
print(ca_nhan)