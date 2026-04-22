def tinh_luy_thua_1(a, b, n):
    return a**(b + n)
def tinh_luy_thua_2(b, n, a):
    return b**(n + 2**a)
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
n = float(input("Nhập số n: "))
print("-" * 30)
print(f"Tổng a + b = {a + b}")
print(f"Hiệu a - b = {a - b}")
print(f"Tích a x b = {a * b}")
if b != 0:
    print(f"Thương a / b = {a / b}")
else:
    print(f"Yêu cầu nhập lại")
print("-" * 30)
kq1 = tinh_luy_thua_1(a, b, n)
kq2 = tinh_luy_thua_2(b, n, a)
print(f"Kết quả lũy thừa a^(b+n) là: {kq1}")
print(f"Kết quả lũy thừa b^(n+2^a) là: {kq2}")
