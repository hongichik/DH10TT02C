kho={"táo": 50, "chuối": 30, "cam": 21}
print("Danh sách kho ban đầu: ", kho)
kho["chuối"]=10
print("Danh sách kho sau khi cập nhật chuối:", kho)
kho["nho"]=15
print("Danh sách kho sau khi thêm nho:", kho )
tong=sum(kho.values())
print(f"Danh sách tổng sản phẩm trong kho: {tong}")