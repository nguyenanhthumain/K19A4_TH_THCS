def nam_nhuan(y):
    return (y%4==0 and y%100!=0) or (y%400==0)

def so_ngay(m, y):
    if m in [1,3,5,7,8,10,12]:
        return 31
    elif m in [4,6,9,11]:
        return 30
    else:
        return 29 if nam_nhuan(y) else 28