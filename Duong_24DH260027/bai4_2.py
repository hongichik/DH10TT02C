ca_nhan={"ten":"Duc Duong", "tuoi": 20, "nghe_nghiep":"Sinh vien"}
print("Danh sách thông tin cá nhân ban đầu:", ca_nhan)
ca_nhan["email"]="duongvipubqn@gmail.com"
print("Danh sách thông tin cá nhân sau khi thêm email:", ca_nhan)
ca_nhan["tuoi"]=21
print("Danh sách thông tin cá nhân sau khi thay tuổi:", ca_nhan)
ca_nhan.pop("nghe_nghiep")
print("Danh sách thông tin cá nhân sau khi xóa nghề nghiệp:", ca_nhan)