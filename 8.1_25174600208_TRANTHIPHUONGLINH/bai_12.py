# Bai 12
def nhap_nhan_vien():
    ten = input("Ten: ")
    que = input("Que: ")
    nam = int(input("Tham nien: "))
    return ten, que, nam

def tinh_luong_nhan_vien(nam):
    return 3000000 + nam * 500000

def xuat_nhan_vien(ten, que, nam, luong):
    print("Ten:", ten)
    print("Que:", que)
    print("Nam:", nam)
    print("Luong:", luong)

ten, que, nam = nhap_nhan_vien()
luong = tinh_luong_nhan_vien(nam)
xuat_nhan_vien(ten, que, nam, luong)