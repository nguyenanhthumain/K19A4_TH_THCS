def so_ngay_trong_thang(thang, nam):
    nam_nhuan = (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
    
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        return 29 if nam_nhuan else 28
    else:
        return None 

try:
    thang = int(input("Nhập tháng (1-12): "))
    nam = int(input("Nhập năm: "))
    so_ngay = so_ngay_trong_thang(thang, nam)
    if so_ngay is None:
        print("Tháng không hợp lệ!")
    else:
        print(f"Số ngày trong tháng {thang} năm {nam} là: {so_ngay}")
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ.")
