def la_nam_nhuan(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def so_ngay(thang, nam):
    if thang in [1,3,5,7,8,10,12]:
        return 31
    elif thang in [4,6,9,11]:
        return 30
    elif thang == 2:
        if la_nam_nhuan(nam):
            return 29
        else:
            return 28
    else:
        return "Tháng không hợp lệ"

# chạy
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))
print("Số ngày:", so_ngay(m, y))