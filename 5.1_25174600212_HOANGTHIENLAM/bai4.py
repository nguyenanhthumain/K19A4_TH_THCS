while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    if 0 < m < n:
        break
    else:
        print("Sai điều kiện, nhập lại!")
ds = []
i = m
while i <= n and len(ds) < 100:
    ds.append(i)
    i += 2
tong = 0
for x in ds:
    tong += x
print("Danh sách:", ds)
print("Tổng:", tong)