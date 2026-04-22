def nam_nhuan(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def so_ngay(m, y):
    if m == 2:
        return 29 if nam_nhuan(y) else 28
    if m in [4,6,9,11]:
        return 30
    return 31

y = int(input("Năm: "))
m = int(input("Tháng: "))

print("Năm nhuận" if nam_nhuan(y) else "Không nhuận")
print("Số ngày:", so_ngay(m, y))