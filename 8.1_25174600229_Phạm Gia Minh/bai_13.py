def la_nam_nhuan(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

def so_ngay_trong_thang(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]: return 31
    if m in [4, 6, 9, 11]: return 30
    if m == 2:
        return 29 if la_nam_nhuan(y) else 28
    return 0

y = int(input("Nhập năm: "))
m = int(input("Nhập tháng: "))
print(f"Năm {y} là năm nhuận: {la_nam_nhuan(y)}")
print(f"Tháng {m}/{y} có {so_ngay_trong_thang(m, y)} ngày.")