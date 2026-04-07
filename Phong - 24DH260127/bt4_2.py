ca_nhan = {
    "ten":"phong",
    "tuoi":20,
    "nghe_nghiep":"Sinh viên",
}

print(ca_nhan)

ca_nhan["email"]="dp28012k62k6@gmail.com"

print(ca_nhan)

ca_nhan["tuoi"] = 20
print(ca_nhan)

ca_nhan.pop("nghe_nghiep")
print(ca_nhan)