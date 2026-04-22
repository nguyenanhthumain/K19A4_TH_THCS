#cau13
def la_nam_nhuan(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    return False

def so_ngay(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        if la_nam_nhuan(y):
            return 29
        else:
            return 28
    else:
        return -1

thang = int(input("Nhap thang: "))
nam = int(input("Nhap nam: "))

ngay = so_ngay(thang, nam)

if ngay != -1:
    print(f"Thang {thang} nam {nam} co {ngay} ngay.")
else:
    print("Thang khong hop le!")