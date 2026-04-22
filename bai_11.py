def nhap():
    ten = input("Tên: ")
    toan = float(input())
    ly = float(input())
    hoa = float(input())
    return ten, toan, ly, hoa

def tb(t, l, h):
    return (t+l+h)/3

def xuat():
    ten, t, l, h = nhap()
    print(ten, tb(t, l, h))

xuat()