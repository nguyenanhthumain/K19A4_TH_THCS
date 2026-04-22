#cau3
n = int(input("Nhap do dai n: "))
ds = []
for i in range(n):
    ds.append((i * 12345 + 6789) % 50 + 1)

print("Danh sach:", ds)
print("Cac so nguyen to trong danh sach:")

for x in ds:
    if x < 2:
        continue
    la_nt = True
    for i in range(2, x):
        if x % i == 0:
            la_nt = False
            break
    if la_nt:
        print(x, end=" ")