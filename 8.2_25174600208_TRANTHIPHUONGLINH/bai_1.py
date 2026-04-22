#bai1
def kiem_tra_nam_nhuan(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    return False

def dem_ngay(thang, nam):
    ngay_31 = [1, 3, 5, 7, 8, 10, 12]
    ngay_30 = [4, 6, 9, 11]

    if thang in ngay_31:
        return 31
    elif thang in ngay_30:
        return 30
    elif thang == 2:
        return 29 if kiem_tra_nam_nhuan(nam) else 28
    else:
        return -1

t = int(input("Tháng: "))
n = int(input("Năm: "))
print("Kết quả:", dem_ngay(t, n))