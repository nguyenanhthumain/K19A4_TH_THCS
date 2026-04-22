"""Bài 3. Hãy viết hàm tạo 1 danh sách có độ dài là n với n nhập từ bàn phím với
các phần tử trong danh sách đó được khởi tạo ngẫu nhiên (được phép sử dụng
hàm random trong Python) và in ra các phần tử của mảng sau đó thoả mãn là số
nguyên tố."""

import random

def tao_mang(n):
    mang = [random.randint(1, 1000) for _ in range(n)]
    return mang

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập n: "))
mang = tao_mang(n)
print("Các phần tử trong mảng:")
for x in mang:
    print(x, end=" ")
print()

print("Các số nguyên tố trong mảng:")
for x in mang:
    if la_so_nguyen_to(x):
        print(x, end=" ")
print()