danh_ba={" linh": "0901234567", "Anh": "0912345678", "Cao": "0923456789"}
print ("Danh sách danh bạ ban đầu: ", danh_ba)
if "Anh" in danh_ba:
    print(f"Số điện thoại của Anh: {danh_ba["Anh"]}" )
if "Cao" in danh_ba:
    del danh_ba["Cao"]
print("Danh sách danh bạ sau khi xóa Cao:", danh_ba)