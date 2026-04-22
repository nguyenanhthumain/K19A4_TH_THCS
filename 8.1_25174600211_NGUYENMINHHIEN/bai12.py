def nhap():
    hoten = input("Nhap ho ten: ")
    que = input("Nhap que quan: ")
    tham_nien = int(input("Nhap tham nien (nam): "))
    return hoten, que, tham_nien
def tinh_luong(tham_nien):
    luong_cb = 3000000
    return luong_cb + tham_nien * 500000
def xuat(hoten, que, tham_nien, luong):
    print("Ho ten:", hoten)
    print("Que quan:", que)
    print("Tham nien:", tham_nien)
    print("Luong:", luong)
ht, q, tn = nhap()
luong = tinh_luong(tn)
xuat(ht, q, tn, luong)