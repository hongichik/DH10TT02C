sdt={
    "An": "0901234567",
    "Binh": "0912345678",
    "Cuong": "0923456789"
}
if "Binh" in sdt:
    print("so dien thoai Binh",sdt["Binh"])
del sdt["Cuong"]
print("sdt sau khi cap nhat",sdt)