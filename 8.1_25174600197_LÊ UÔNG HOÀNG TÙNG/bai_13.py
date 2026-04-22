def nam_nhuan(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    return False
def so_ngay_thang(m, y):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    elif m == 2:
        if nam_nhuan(y):
            return 29
        else:
            return 28
    else:
        return 0
def bai_13():
    y = int(input(" nam: "))
    m = int(input(" thang: "))
    if nam_nhuan(y):
        print("nam nhuan")
    else:
        print("khong phai nam nhuan")

    print("so ngay trong thang:", so_ngay_thang(m,y))
bai_13()