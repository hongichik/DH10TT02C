phone = {"An": "0901234567", "Bình": "0912345678", "Cường": "0923456789"}

if "Bình" in phone:
    print(phone["Bình"])

del phone["Cường"]
print(phone)