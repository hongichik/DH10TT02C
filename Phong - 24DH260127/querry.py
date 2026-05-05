from quanlyNV import QLNV

nv = QLNV("Sanpham/nhanvien.csv", title=["manv","ho_ten","sdt","diachi","chucvu"])

while True:
    lua_chon = input(" chức năng: 1. Tìm kiếm , 2. Xóa, 3.Cập nhật , 4. Thêm , 0. Thoát: ")
    if lua_chon == '0':
        break
    elif lua_chon == '1':
        title_keyword = input("Nhập tiêu đề tìm kiếm: ")
        keyword = input("Nhập từ khóa tìm kiếm: ")
        results = nv.timkiem(title_keyword, keyword)
        print(results['data'])
    elif lua_chon == '2':
        manv = input("Nhập mã nhân viên cần xoá: ")
        nv.xoa("manv", manv)
    elif lua_chon == '3':
        manv = input("Nhập mã nhân viên cần sửa: ")
        keyword = input("Nhập từ khóa tìm kiếm: ")
        title_edit = input("Nhập tiêu đề cần sửa : ").split(',')
        new_data = input("Nhập dữ liệu mới : ").split(',')
        nv.capnhat("manv", manv, title_edit, new_data)
    elif lua_chon == '4':
        manv = input("Nhập mã nhân viên: ")
        ho_ten = input("Nhập họ tên nhân viên: ")
        sdt = input("Nhập số điện thoại: ")
        diachi = input("Nhập địa chỉ: ")
        chucvu = input("Nhập chức vụ: ")
        nv.them([manv, ho_ten, sdt, diachi, chucvu])
