def la_nam_nhuan(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    return False
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
    return 0
year = int(input("Nhập năm y: "))
month = int(input("Nhập tháng m: "))
if la_nam_nhuan(year):
    print(f"Năm {year} là năm nhuận.")
else:
    print(f"Năm {year} không phải là năm nhuận.")
ngay_max = so_ngay_trong_thang(month, year)
if ngay_max > 0:
    print(f"Tháng {month} năm {year} có tối đa {ngay_max} ngày.")
else:
    print(f"Yêu cầu nhập lại")
