def so_ngay_trong_thang(thang, nam):
    if thang in [1,3,5,7,8,10,12]:
        return 31
    elif thang in [4,6,9,11]:
        return 30
    elif thang == 2:
        if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
            return 29
        return 28
    else:
        return -1
t = int(input("Nhap thang: "))
n = int(input("Nhap nam: "))
print("So ngay:", so_ngay_trong_thang(t,n))