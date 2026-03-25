m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
kq = 0

while n > 0:
    if n % 2 == 1:
        kq += m
    m *= 2
    n //= 2

print("Kết quả:", kq)