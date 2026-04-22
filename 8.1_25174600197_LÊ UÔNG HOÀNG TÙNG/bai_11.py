def nhap():
    ten = input(" ho ten: ")
    toan = float(input("diem toan: "))
    ly = float(input("diem ly: "))
    hoa = float(input("diem hoa: "))
    return ten, toan, ly, hoa
def trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3
def xuat(ten, tb):
    print("ho ten:", ten)
    print("diem trung binh:", tb)
def bai_11():
    ten, toan, ly, hoa = nhap()
    tb = trung_binh(toan, ly, hoa)
    xuat(ten, tb)
bai_11()