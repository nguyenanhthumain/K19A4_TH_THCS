def nhap():
    hoten = input("Nhap ho ten: ")
    toan = float(input("Nhap diem Toan: "))
    ly = float(input("Nhap diem Ly: "))
    hoa = float(input("Nhap diem Hoa: "))
    return hoten, toan, ly, hoa
def tinh_tb(toan, ly, hoa):
    return (toan + ly + hoa) / 3
def xuat(hoten, tb):
    print("Ho ten:", hoten)
    print("Diem trung binh:", round(tb, 2))
ht, t, l, h = nhap()
tb = tinh_tb(t, l, h)
xuat(ht, tb)