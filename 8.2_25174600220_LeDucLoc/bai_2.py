"""Bài 2. Hãy viết hàm tạo 1 danh sách có độ dài là n với n nhập từ bàn phím với
các phần tử trong danh sách đó được khởi tạo ngẫu nhiên (được phép sử dụng
hàm random trong Python). Trong hàm này, hãy sử dụng lambda để tính bình
phương của các số trong danh sách."""

import random

n = int(input("Nhap n: "))
a = [random.randint(1, 100) for i in range(n)]
print(a)

b = list(map(lambda x: x**2, a))
print(b)