danhba = {
    "An": "0901234567",
    "Binh": "0912345678",
    "Cuong": "0923456789"
}
if "Binh" in danhba:
    print(danhba["Binh"])
if "Cuong" in danhba:
    del danhba["Cuong"]
print(danhba)