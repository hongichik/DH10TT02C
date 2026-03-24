sv = {"id": "24DH360067", "name": "Anh Nam Dinh", "age": 18, "gpa": 6.7}
sv["major"] = "CNTT"
sv["gpa"] += 0.5
for key, value in sv.items():
    print(key,":", value)