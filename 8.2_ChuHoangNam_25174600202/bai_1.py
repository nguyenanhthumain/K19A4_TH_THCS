#cau1
def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
            return 29
        else:
            return 28
    else:
        return "thang khong hop le"
t = int(input("nhap thang: "))
n = int(input("nhap nam: "))
print("so ngay la:", so_ngay_trong_thang(t, n))