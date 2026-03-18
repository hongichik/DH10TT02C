ca_nhan={
    "ten":"Nguyen Minh Duc",
    "tuoi":20,
    "nghe_nghiep":"sinh vien",
}
print(ca_nhan)

ca_nhan["email"]= "ducken4321@gmail.com"

print(ca_nhan)

ca_nhan["tuoi"]=25
print(ca_nhan)

ca_nhan.pop("nghe_nghiep")
print(ca_nhan)