# Bai 13

def kiem_tra_nam_nhuan(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    return False
def so_ngay_trong_thang(m, y):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    elif m == 2:
        if kiem_tra_nam_nhuan(y):
            return 29
        return 28

m = int(input())
y = int(input())

print(so_ngay_trong_thang(m, y))