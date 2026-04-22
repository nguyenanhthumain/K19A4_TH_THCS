def nam_nhuan(y):
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
def so_ngay_thang(m, y):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    elif m == 2:
        return 29 if nam_nhuan(y) else 28
    else:
        return 0

y = int(input("Nhập năm: "))
m = int(input("Nhập tháng: "))
print("Năm nhuận:" , nam_nhuan(y))
print("Số ngày:", so_ngay_thang(m, y))