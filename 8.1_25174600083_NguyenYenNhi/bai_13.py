#bai_13 
"""
Viết chương trình bao gồm các hàm sau:
+ Hàm kiểm tra năm y cho trước có nhuận hay không.
+ Hàm xác định số ngày tối đa của tháng m trong năm y cho trước.
"""
def nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    else:
        return False
nam = int(input("Nhập năm: "))
if nam_nhuan(nam):
    print(f"{nam} là năm nhuận")
else:
    print(f"{nam} không phải là năm nhuận")

    
def so_ngay_toi_da(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if nam_nhuan(nam):
            return 29
        else:
            return 28
    else:
        return "Tháng không hợp lệ"
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
print(f"Số ngày tối đa của tháng {thang} năm {nam} là: {so_ngay_toi_da(thang, nam)}")
