def nam_nhuan(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    return False

def so_ngay_trong_thang(m, y):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    if m == 2:
        if nam_nhuan(y):
            return 29
        else:
            return 28
    return -1  

def a():
    y = int(input("Nhập năm: "))
    m = int(input("Nhập tháng: "))
    if nam_nhuan(y):
        print(y, "là năm nhuận")
    else:
        print(y, "không phải năm nhuận")
    kq = so_ngay_trong_thang(m, y)
    if kq == -1:
        print("Yêu cầu nhập lại")
    else:
        print("Số ngày trong tháng là:", kq)
a()