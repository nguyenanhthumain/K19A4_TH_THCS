#cau11
def nhap_info():
    ten = input("Nhap ho ten: ")
    toan = float(input("Nhap diem Toan: "))
    ly = float(input("Nhap diem Ly: "))
    hoa = float(input("Nhap diem Hoa: "))
    return ten, toan, ly, hoa

def tinh_tb(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def xuat_kq(ten, toan, ly, hoa, tb):
    print("\n--- KET QUA ---")
    print(f"Ho ten: {ten}")
    print(f"Diem: Toan {toan}, Ly {ly}, Hoa {hoa}")
    print(f"Diem trung binh: {tb:.2f}")

ten, toan, ly, hoa = nhap_info()
tb = tinh_tb(toan, ly, hoa)
xuat_kq(ten, toan, ly, hoa, tb)