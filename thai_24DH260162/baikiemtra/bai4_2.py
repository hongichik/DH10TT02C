ca_nhan={"ten":"Thai Nguyen", "tuoi": 20, "nghe_nghiep":"Sinh vien"}
print("Danh sách thông tin cá nhân ban đầu:", ca_nhan)
ca_nhan["email"]="barodick.db@gmail.com"
print("Danh sách thông tin cá nhân khi thêm email:", ca_nhan)
ca_nhan["tuoi"]=21
print("Danh sách thông tin cá nhân khi thay tuổi:", ca_nhan)
ca_nhan.pop("nghe_nghiep")
print("Danh sách thông tin cá nhân khi xóa nghề nghiệp:", ca_nhan)