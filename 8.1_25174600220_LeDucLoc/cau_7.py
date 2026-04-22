"""Bài 7:
a) Viết chương trình tìm ước chung lớn nhất của 2 số a, b.
b) Xây chương trình tìm bội chung nhỏ nhất của 2 số a, b.
c) Viết chương trình cho phép thực hiện rút gọn phân số.
Hướng dẫn:
+ Tìm UCLN của tử số và mẫu số.
+ Chia tử và mẫu của phân số cho UCLN vừa tìm được.
d) Viết chương trình nhập vào n số nguyên và in ra các số nhỏ nhất và lớn nhất
trong các số đó."""

#a
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
print(f"UCLN của {a} và {b} là: {max(a, b)}")   
#b
print(f"BCNN của {a} và {b} là: {min(a, b)}")
#c
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))
print(f"UCLN của {c} và {d} là: {max(c, d)}")   
print(f"BCNN của {c} và {d} là: {min(c, d)}")
#d
n = int(input("Nhập số lượng số nguyên: "))
numbers = []
for i in range(n):
    num = int(input(f"Nhập số nguyên thứ {i + 1}: "))
    numbers.append(num)
min_number = min(numbers)
max_number = max(numbers)
print(f"Số nguyên nhỏ nhất là: {min_number}")
print(f"Số nguyên lớn nhất là: {max_number}")