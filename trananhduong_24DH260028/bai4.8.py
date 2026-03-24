ds_sv = [
    {"name": "An", "age": 20, "score": 8.0},
    {"name": "Binh", "age": 21, "score": 9.5},
    {"name": "Cuong", "age": 19, "score": 7.5}
]
sv_gioi_nhat = max(ds_sv, key=lambda x: x["score"])
print("sv_gioi_nhat")
for sv  in ds_sv: sv["age"] += 1
print(ds_sv)