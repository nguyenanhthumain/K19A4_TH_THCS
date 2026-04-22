a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
n = int(input("Nhập n: "))

print("Tổng:", a + b)
print("Hiệu:", a - b)
print("Tích:", a * b)

if b != 0:
    print("Thương:", a / b)
else:
    print("Không thể chia cho 0")

print("a^(b+n) =", a ** (b + n))
print("b^(n+2^a) =", b ** (n + 2 ** a))