ds_sinh_vien=[{" name":"Anh", "age":20,"score":8.0}, {"name":"Beo", "age":21, "score": 9.5}, {"name":"Phong", "age":19, "score": 7.5}]
print ("Danh sách sinh viên ban đầu", ds_sinh_vien)
sv_max=max(ds_sinh_vien, key=lambda x: x["score"])
print (f"Sinh viên có điểm cao nhất: {sv_max['name']} với {sv_max['score']} điểm.")
for sv in ds_sinh_vien:
    sv["age"]+=1
print ("Danh sách sinh viên sau khi cập nhật: ", ds_sinh_vien)