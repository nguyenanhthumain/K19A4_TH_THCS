def nhap_nv():
    ten = input(" ho ten: ")
    que = input(" que quan: ")
    tham_nien = int(input(" tham nien: "))
    return ten, que, tham_nien
def tinh_luong(tham_nien):
    luong_co_ban = 1000
    return luong_co_ban + tham_nien * 200
def xuat_nv(ten, que, tham_nien, luong):
    print("ten:", ten)
    print("que:", que)
    print("tham nien:", tham_nien)
    print("luong:", luong)
def bai_12():
    ten, que, tham_nien = nhap_nv()
    luong = tinh_luong(tham_nien)
    xuat_nv(ten, que, tham_nien, luong)
bai_12()