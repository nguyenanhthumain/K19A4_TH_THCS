#bai_2
"""
Hãy viết hàm tạo 1 danh sách có độ dài là n với n nhập từ bàn phím với
các phần tử trong danh sách đó được khởi tạo ngẫu nhiên (được phép sử dụng
hàm random trong Python). Trong hàm này, hãy sử dụng lambda để tính bình
phương của các số trong danh sách.
"""


def danh_sach(n):
    import random
    ds = [random.randint(1, 100) for _ in range(n)]
    print("Danh sách ban đầu:", ds)
    binh_phuong = list(map(lambda x: x**2, ds))
    print("Bình phương của các số là:", binh_phuong)
n = int(input("Nhập độ dài của danh sách: "))

danh_sach(n)
