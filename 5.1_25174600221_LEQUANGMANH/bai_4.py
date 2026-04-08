while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    if 0 < m < n:
        break
    print("Sai điều kiện!")

lst = []
count = 0
i = m

while i <= n and count < 100:
    lst.append(i)
    i += 2
    count += 1

tong = 0
for x in lst:
    tong += x

print("Danh sách:", lst)
print("Tổng:", tong)