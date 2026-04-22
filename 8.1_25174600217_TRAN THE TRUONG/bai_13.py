def nam_nhuan(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    return False

def so_ngay_trong_thang(m, y):
    if m < 1 or m > 12:
        return -1

    if m in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif m in (4, 6, 9, 11):
        return 30
    else:
        if nam_nhuan(y):
            return 29
        else:
            return 28

def main():
    y = int(input("Nhập năm y: "))
    m = int(input("Nhập tháng m: "))

    if nam_nhuan(y):
        print(y, "là năm nhuận")
    else:
        print(y, "không phải năm nhuận")

    ngay = so_ngay_trong_thang(m, y)
    if ngay == -1:
        print("Tháng không hợp lệ")
    else:
        print("Tháng", m, "năm", y, "có", ngay, "ngày")
main()