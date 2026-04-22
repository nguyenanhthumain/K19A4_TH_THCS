def nhap_thong_tin():
    ten = input("Nhập học tên: ")
    toan = float(input("Điểm toán: "))
    ly = float(input("Điểm lý: "))
    hoa = float(input("Điểm hóa: "))
    return ten, toan, ly, hoa
def tinh_diem_tb(toan, ly, hoa):
    return(toan + ly + hoa) / 3
def xuat(ten, diem_tb):
    print("Họ tên:", ten)
    print("Điểm trung bình:", diem_tb)

ten, toan, ly, hoa = nhap_thong_tin()
diem_tb = tinh_diem_tb(toan, ly, hoa)
xuat(ten, diem_tb)