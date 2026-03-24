sinhvien={
    "maso": "SV001",
    "ten": "An",
    "tuoi": 20,
    "diem_tb": 8.5
}
sinhvien["nganhhoc"]= "CNTT"
sinhvien["diem_tb"] += 0.5
for key, value in sinhvien.items():
    print(key, ":", value)