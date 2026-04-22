#bai_1
"""
Viết một hàm có tên so_ngay_trong_thang nhận vào tháng và năm nhập
từ bàn phím và trả về số ngày trong tháng đó. (Chú ý xử lý năm nhuận)
"""

def so_ngay_trong_thang(thang,nam):
    if thang in [1,3,5,7,8,10,12]:
        return 31
    elif thang in [4,6,9,11]:
        return 30  
    elif thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            return 29
        else:
            return 28
    else:
        print("Tháng không hợp lệ")
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))  
so_ngay = so_ngay_trong_thang(thang, nam)
print(f"Số ngày trong tháng {thang} năm {nam} là: {so_ngay}")