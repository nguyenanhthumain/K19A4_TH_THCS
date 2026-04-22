def nhap_nv():
    ten = input("Họ tên: ")
    que = input("Quê quán: ")
    tham_nien = int(input("Thâm niên (năm): "))
    return ten, que, tham_nien
def tinh_luong(tham_nien):
    luong_co_ban = 1000
    return luong_co_ban + tham_nien * 200
def xuat_nv(ten, que, tham_nien, luong):
    print("Họ tên:", ten)
    print("Quê:", que)
    print("Thâm niên:", tham_nien)
    print("Lương:", luong)

ten, que, tn = nhap_nv()
luong = tinh_luong(tn)
xuat_nv(ten, que, tn, luong)