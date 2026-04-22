"""Bài 5. Hãy viết hàm tạo 1 danh sách có độ dài là n với n nhập từ bàn phím với
các phần tử trong danh sách đó được khởi tạo ngẫu nhiên (được phép sử dụng
hàm random trong Python) và sử dụng lambda để trả về True nếu số đó là chẵn,
ngược lại trả về False."""

import random
n = int(input("Nhap n: "))
a = [random.randint(1, 100) for i in range(n)]
print(a)
print(list(map(lambda x: x % 2 == 0, a)))