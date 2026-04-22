def nhap_thong_tin():
    ten = input("Nhập họ tên nhân viên: ")
    que = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên công tác (số năm): "))
    return ten, que, tham_nien
def tinh_luong(tham_nien):
    luong_co_ban = 5000000
    phu_cap_moi_nam = 500000
    tong_luong = luong_co_ban + (tham_nien * phu_cap_moi_nam)
    return tong_luong
def xuat_thong_tin(ten, que, tham_nien, luong):
    print("-" * 30)
    print("THÔNG TIN NHÂN VIÊN")
    print(f"Họ tên: {ten}")
    print(f"Quê quán: {que}")
    print(f"Thâm niên: {tham_nien} năm")
    print(f"Lương: {luong:,} VNĐ") 
ten_nv, que_nv, tn_nv = nhap_thong_tin()
luong_nv = tinh_luong(tn_nv)
xuat_thong_tin(ten_nv, que_nv, tn_nv, luong_nv)
