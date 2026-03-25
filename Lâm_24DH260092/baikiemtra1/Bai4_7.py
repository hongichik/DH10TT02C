kho ={
    "apple":50,
    "banana":30,
    "mango":20,
}
# Giảm số lượng banana xuống 10
kho["banana"]=10
print(kho)
#Thêm sản phẩm grape=15
kho["grape"]=15
print(kho)
#Tổng số lượng
tong_sl=sum(kho.values())
print(tong_sl)