danh_ba={"An": "0901234567", "Bình": "0912345678", "Cường": "0923456789"}
print ("Danh sách danh bạ ban đầu: ", danh_ba)
if "Bình" in danh_ba:
    print(f"Số điện thoại của Bình: {danh_ba["Bình"]}" )
if "Cường" in danh_ba:
    del danh_ba["Cường"]
print("Danh sách danh bạ sau khi xóa Cường:", danh_ba)