def so_ngay_trong_thang(thang, nam):
    if thang < 1 or thang > 12:
        print("Tháng không hợp lệ")
        return
    if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
        nam_nhuan = True
        print("Đây là năm nhuận")
    else:
        nam_nhuan = False
        print("Đây không phải năm nhuận")
    if thang == 2:
        if nam_nhuan:
            print("Tháng", thang, "có 29 ngày")
        else:
            print("Tháng", thang, "có 28 ngày")
    elif thang in [4, 6, 9, 11]:
        print("Tháng", thang, "có 30 ngày")
    else:
        print("Tháng", thang, "có 31 ngày")

thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
so_ngay_trong_thang(thang, nam)