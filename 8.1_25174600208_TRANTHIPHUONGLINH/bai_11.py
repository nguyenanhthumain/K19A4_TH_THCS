# Bai 11
def nhap_thong_tin():
    ten = input("Ten: ")
    toan = float(input("Toan: "))
    ly = float(input("Ly: "))
    hoa = float(input("Hoa: "))
    return ten, toan, ly, hoa

def tinh_diem_trung_binh(t, l, h):
    return (t + l + h) / 3

def xuat_thong_tin(ten, tb):
    print("Ten:", ten)
    print("Diem TB:", tb)

ten, t, l, h = nhap_thong_tin()
tb = tinh_diem_trung_binh(t, l, h)
xuat_thong_tin(ten, tb)