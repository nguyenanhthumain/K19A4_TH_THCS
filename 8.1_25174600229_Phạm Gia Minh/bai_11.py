def nhap_sv():
    ten = input("Họ tên: ")
    toan = float(input("Điểm Toán: "))
    ly = float(input("Điểm Lý: "))
    hoa = float(input("Điểm Hóa: "))
    return {"ten": ten, "toan": toan, "ly": ly, "hoa": hoa}

def tinh_tb(sv):
    return (sv['toan'] + sv['ly'] + sv['hoa']) / 3

def xuat_sv(sv):
    tb = tinh_tb(sv)
    print(f"SV: {sv['ten']} - ĐTB: {tb:.2f}")

sv = nhap_sv()
xuat_sv(sv)