def nhap_thong_tin():
    ho_ten = input("Họ và tên: ")
    toan = float(input("điểm Toán: "))
    ly = float(input("điểm Lý: "))
    hoa = float(input("điểm Hóa: "))
    return ho_ten, toan, ly, hoa

def tinh_trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def xuat_thong_tin(ho_ten, toan, ly, hoa, dtb):
    print("\nKết quả")
    print("Họ tên:", ho_ten)
    print("Điểm Toán:", toan)
    print("Điểm Lý:", ly)
    print("Điểm Hóa:", hoa)
    print("Điểm trung bình:", dtb)

def main():
    ho_ten, toan, ly, hoa = nhap_thong_tin()
    dtb = tinh_trung_binh(toan, ly, hoa)
    xuat_thong_tin(ho_ten, toan, ly, hoa, dtb)
main()