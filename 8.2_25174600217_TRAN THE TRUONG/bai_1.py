def so_ngay_trong_thang(thang, nam):
    def nam_nhuan(n):
        return (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0)

    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if nam_nhuan(nam) else 28
    else:
        return None

thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
kq = so_ngay_trong_thang(thang, nam)
print("Số ngày:", kq)