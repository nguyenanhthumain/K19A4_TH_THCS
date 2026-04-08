n = int(input("Nhập n: "))
ds = []
for i in range(1, n + 1):
    ds.append(i * i)
m = int(input("Nhập m: "))
if m >= n:
    print([])
else:
    print(ds[m:])