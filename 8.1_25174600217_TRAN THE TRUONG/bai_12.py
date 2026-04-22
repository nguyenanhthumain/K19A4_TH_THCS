def nhap_nhan_vien():
    ho_ten = input("Nhập họ tên: ")
    que_quan = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên công tác (năm): "))
    return ho_ten, que_quan, tham_nien

def tinh_luong(tham_nien):
    luong_co_ban = 7500000
    phu_cap = tham_nien * 1000000
    return luong_co_ban + phu_cap

def xuat_nhan_vien(ho_ten, que_quan, tham_nien, luong):
    print("\n===== THÔNG TIN NHÂN VIÊN =====")
    print("Họ tên:", ho_ten)
    print("Quê quán:", que_quan)
    print("Thâm niên công tác:", tham_nien, "năm")
    print("Lương:", luong)

def main():
    ho_ten, que_quan, tham_nien = nhap_nhan_vien()
    luong = tinh_luong(tham_nien)
    xuat_nhan_vien(ho_ten, que_quan, tham_nien, luong)
main()