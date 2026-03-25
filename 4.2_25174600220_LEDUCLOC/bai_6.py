#WHILE
n = 0
while n <= 100:
    n = int(input("Nhập số > 100: "))

tong = 0
temp = n
while temp > 0:
    tong += temp % 10
    temp //= 10
print(f"Tổng các chữ số: {tong}")

#FOR
n = input("Nhập số > 100: ")
if int(n) > 100:
    tong = 0
    for kytu in n:
        tong += int(kytu)
    print(f"Tổng các chữ số: {tong}")