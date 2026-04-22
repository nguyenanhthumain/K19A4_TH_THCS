"""Bài 11: Viết chương trình nhập Họ tên, điểm Toán, điểm Lý, điểm Hóa của một
sinh viên. Yêu cầu: Viết hàm nhập, xuất, tính trung bình để tính điểm trung bình
và xuất ra kết quả."""

def nhap_thong_tin():
    ho_ten = input("Nhập họ tên sinh viên: ")
    diem_toan = float(input("Nhập điểm Toán: "))
    diem_ly = float(input("Nhập điểm Lý: "))
    diem_hoa = float(input("Nhập điểm Hóa: "))
    return ho_ten, diem_toan, diem_ly, diem_hoa

def xuat_thong_tin(ho_ten, diem_toan, diem_ly, diem_hoa):
    print(f"Họ tên: {ho_ten}")
    print(f"Điểm Toán: {diem_toan}")
    print(f"Điểm Lý: {diem_ly}")
    print(f"Điểm Hóa: {diem_hoa}")

def tinh_trung_binh(diem_toan, diem_ly, diem_hoa):
    return (diem_toan + diem_ly + diem_hoa)/3

ho_ten, diem_toan, diem_ly, diem_hoa = nhap_thong_tin()
xuat_thong_tin(ho_ten, diem_toan, diem_ly, diem_hoa)
diem_trung_binh = tinh_trung_binh(diem_toan, diem_ly, diem_hoa)
print(f"Điểm trung bình: {diem_trung_binh}")