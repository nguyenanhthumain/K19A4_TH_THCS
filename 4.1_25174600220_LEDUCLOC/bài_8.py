"""Bài 8: Viết chương trình yêu cầu xuất ra các số từ 1 đến 1000, liệt kê những số là
số nguyên tố."""

print("Cac so nguyen to tu 1 den 1000 la:")

for n in range(1, 1001):
    if n < 2:
        continue

    la_so_nguyen_to = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_so_nguyen_to = False
            break
            
    if la_so_nguyen_to:
        print(n, end=" ")