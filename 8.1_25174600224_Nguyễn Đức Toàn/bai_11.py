def nhap_thong_tin():
    ten = input("Nhập họ tên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    return ten, toan, ly, hoa

def trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def xuat_thong_tin(ten, toan, ly, hoa, tb):
    print("Họ tên:", ten)
    print("Toán:", toan)
    print("Lý:", ly)
    print("Hóa:", hoa)
    print("Trung bình:", tb)

def a():
    ten, toan, ly, hoa = nhap_thong_tin()
    tb = trung_binh(toan, ly, hoa)
    xuat_thong_tin(ten, toan, ly, hoa, tb)
a()