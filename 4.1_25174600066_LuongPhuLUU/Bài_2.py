m = int(input("Nhập số nguyên m: "))
n = int(input("Nhập số nguyên n: "))
if m < n:
    m, n = n, m
while m != n:
    if m > n:
        r = m - n
        m = r
    else:
        r = n - m
        n = r
print("UCLN cỉa hai số là:", m)