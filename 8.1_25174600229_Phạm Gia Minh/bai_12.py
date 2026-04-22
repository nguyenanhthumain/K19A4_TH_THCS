def nhap_nv():
    ten = input("Họ tên: ")
    que = input("Quê quán: ")
    nam = int(input("Thâm niên (năm): "))
    return [ten, que, nam]

def tinh_luong(tham_nien):
    luong_co_ban = 5000000
    if tham_nien < 5: return luong_co_ban
    return luong_co_ban * 1.5

def xuat_nv(nv):
    luong = tinh_luong(nv[2])
    print(f"NV: {nv[0]} | Quê: {nv[1]} | Thâm niên: {nv[2]} năm | Lương: {luong:,.0f} VNĐ")

nv = nhap_nv()
xuat_nv(nv)