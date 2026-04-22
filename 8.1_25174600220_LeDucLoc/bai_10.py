"""Bài 10: Viết chương trình nhập từ bàn phím số nguyên dương n và in ra màn hình
các ước số của n."""

n = int(input("Nhập một số nguyên dương n: "))
print(f"Các ước số của {n} là: ", end='')
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')   