def nhap_nv():
    ten = input()
    que = input()
    nam = int(input())
    return ten, que, nam

def tinh_luong(nam):
    return 3000000 + nam*500000

def xuat_nv():
    ten, que, nam = nhap_nv()
    luong = tinh_luong(nam)
    print(ten, que, nam, luong)

xuat_nv()