#cau12
def nhap_nhan_vien():
    ten = input("Nhap ho ten: ")
    que = input("Nhap que quan: ")
    tham_nien = int(input("Nhap tham nien (nam): "))
    return ten, que, tham_nien

def tinh_luong(tham_nien):
    # Quy dinh: Luong = 5 trieu + (tham nien * 500.000)
    luong_co_ban = 5000000
    return luong_co_ban + (tham_nien * 500000)

def xuat_nhan_vien(ten, que, tham_nien, luong):
    print("\n--- THONG TIN NHAN VIEN ---")
    print("Ho ten:", ten)
    print("Que quan:", que)
    print("Tham nien:", tham_nien, "nam")
    print("Luong:", luong)

ten, que, tham_nien = nhap_nhan_vien()
luong = tinh_luong(tham_nien)
xuat_nhan_vien(ten, que, tham_nien, luong)
