def nhap_thong_tin():
    ho_ten = input("Nhập họ tên sinh viên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    return ho_ten, toan, ly, hoa
def tinh_trung_binh(t, l, h):
    return (t + l + h) / 3
def xuat_ket_qua(ten, dtb):
    print("-" * 30)
    print(f"Sinh viên: {ten}")
    print(f"Điểm trung bình: {dtb}")
ten, d_toan, d_ly, d_hoa = nhap_thong_tin()
dtb = tinh_trung_binh(d_toan, d_ly, d_hoa)
xuat_ket_qua(ten, dtb)
