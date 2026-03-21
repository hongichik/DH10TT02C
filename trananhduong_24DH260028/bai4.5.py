sv = {
    "id": "SV001",
    "name": "An",
    "age": 20,
    "gpa": 8.5
}
sv["major"] = "CNTT"
sv["gpa"] += 0.5
for key, value in sv.items():
    print(f"{key}: {value}")