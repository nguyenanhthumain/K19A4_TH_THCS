#bai_3
"""
Hãy viết hàm tạo 1 danh sách có độ dài là n với n nhập từ bàn phím với
các phần tử trong danh sách đó được khởi tạo ngẫu nhiên (được phép sử dụng
hàm random trong Python) và in ra các phần tử của mảng sau đó thoả mãn là số
nguyên tố.
"""

def so_nguyen_to(snt):
    if snt < 2:
        return False
    for i in range(2, int(snt**0.5) + 1):
        if snt % i == 0:
            return False
    return True

def danh_sach(n):
    import random
    ds = [random.randint(1, 100) for _ in range(n)]
    print("Danh sách ban đầu:", ds)
    nguyen_to = [x for x in ds if so_nguyen_to(x)]
    print("Các số nguyên tố trong danh sách là:", nguyen_to)
n = int(input("Nhập độ dài của danh sách: "))
danh_sach(n)
