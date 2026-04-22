"""Bài 13: Viết chương trình bao gồm các hàm sau:
+ Hàm kiểm tra năm y cho trước có nhuận hay không.
+ Hàm xác định số ngày tối đa của tháng m trong năm y cho trước."""

#a
def kiem_tra_nam_nhuan(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return True
    return False
nam = int(input("Nhập năm y: "))

if kiem_tra_nam_nhuan(nam):
    print(f"=> Năm {nam} là năm nhuận.")
else:
    print(f"=> Năm {nam} không phải là năm nhuận.")


#b
def so_ngay_toi_da(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if kiem_tra_nam_nhuan(nam):
            return 29
        else:
            return 28
    else:
        return "Tháng không hợp lệ"

thang = int(input("Nhập số tháng: "))
nam = int(input("Nhập số năm: "))
print(f"So ngay trong thang {thang} nam {nam} la: {so_ngay_toi_da(thang, nam)}")