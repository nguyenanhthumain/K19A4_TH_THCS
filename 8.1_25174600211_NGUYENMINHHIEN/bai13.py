def nam_nhuan(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    return False
def so_ngay(thang, nam):
    if thang in [1,3,5,7,8,10,12]:
        return 31
    elif thang in [4,6,9,11]:
        return 30
    elif thang == 2:
        if nam_nhuan(nam):
            return 29
        else:
            return 28
    else:
        return 0
y = int(input("Nhap nam: "))
m = int(input("Nhap thang: "))

if nam_nhuan(y):
    print("Nam nhuan")
else:
    print("Khong phai nam nhuan")
print("So ngay:", so_ngay(m, y))