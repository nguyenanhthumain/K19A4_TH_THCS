def la_nam_nhuan(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
def so_ngay_trong_thang(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        if la_nam_nhuan(y):
            return 29
        else:
            return 28
    else:
        return "Tháng không hợp lệ"
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
ket_qua = so_ngay_trong_thang(thang, nam)
print(f"Số ngày trong tháng {thang}/{nam} là: {ket_qua}")
