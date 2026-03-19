danh_ba={"long": "0901234567", "yen": "0912345678", "duc": "0923456789"}
print ("Danh sách danh bạ ban đầu: ", danh_ba)
if "long" in danh_ba:
    print(f"Số điện thoại của long: {danh_ba["long"]}" )
if "duc" in danh_ba:
    del danh_ba["duc"]
print("Danh sách danh bạ sau khi xóa duc:", danh_ba)