n = input("Nhập số: ")
tong = 0
for d in n:
    tong += int(d)
print("Tổng chữ số:", tong)
#
num = int(input("Nhập số: "))
tong = 0
while num > 0:
    tong += num % 10
    num //= 10
print("Tổng chữ số:", tong)