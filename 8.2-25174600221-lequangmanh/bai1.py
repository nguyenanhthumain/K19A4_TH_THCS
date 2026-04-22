def so_ngay_trong_thang(thang, nam):
    # kiểm tra năm nhuận
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        nhuan = True
    else:
        nhuan = False

    if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
        return 31
    elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
        return 30
    elif thang == 2:
        if nhuan:
            return 29
        else:
            return 28
    else:
        return "Tháng không hợp lệ"


# test
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))
print("Số ngày:", so_ngay_trong_thang(m, y))