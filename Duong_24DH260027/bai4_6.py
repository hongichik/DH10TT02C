sinh_vien={"id": "SV001", "name": "An", "age": 20, "gpa": 8.5}
print ("Danh sách thông tin ban đầu:", sinh_vien)
sinh_vien["major"]="CNTT"
print ("Danh sách thông tin sau khi thêm:", sinh_vien)
sinh_vien["gpa"]+=0.5
print ("Danh sách thông tin sau khi được tăng điêm:", sinh_vien)
print ("Danh sách thông tin chi tiết:")
for key, value in sinh_vien.items(): print (f"{key}: {value}")