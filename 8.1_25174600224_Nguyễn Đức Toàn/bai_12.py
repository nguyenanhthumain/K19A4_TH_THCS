def nhap_nhan_vien():
    ten = input("Nhập họ tên: ")
    que = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên công tác: "))
    return ten, que, tham_nien

def tinh_luong(tham_nien):
    luong_co_ban = 5000000
    phu_cap = tham_nien * 500000
    return luong_co_ban + phu_cap

def xuat_nhan_vien(ten, que, tham_nien, luong):
    print("Họ tên:", ten)
    print("Quê quán:", que)
    print("Thâm niên:", tham_nien, "năm")
    print("Lương:", luong)
    
def a():
    ten, que, tham_nien = nhap_nhan_vien()
    luong = tinh_luong(tham_nien)
    xuat_nhan_vien(ten, que, tham_nien, luong)
a()