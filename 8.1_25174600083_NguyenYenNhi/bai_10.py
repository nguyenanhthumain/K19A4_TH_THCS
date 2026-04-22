#bai_10
"""
Viết chương trình nhập từ bàn phím số nguyên dương n và in ra màn hình
các ước số của n.
"""
def uoc(n):
    ds = []
    for i in range(1, n + 1):
        if n % i == 0:
            ds.append(i)
    return ds
n = int(input("Nhập số nguyên dương n: "))
print(f"Các ước số của {n} là: {uoc(n)}")