# Cách 1 while:
n = int(input("Nhập số nguyên > 100: "))
while n <= 100:
    n = int(input("Nhập lại (phải > 100): "))

tong = 0
temp = n
while temp > 0:
    tong += temp % 10
    temp //= 10

print("Tổng các chữ số của", n, "là:", tong)
# Cách 2 for :

n = int(input("Nhập số nguyên > 100: "))

while n <= 100:
    n = int(input("Nhập lại (phải > 100): "))

tong = 0
temp = n
for _ in range(len(str(n))):
    tong += temp % 10
    temp //= 10

print("Tổng các chữ số của", n, "là:", tong)
