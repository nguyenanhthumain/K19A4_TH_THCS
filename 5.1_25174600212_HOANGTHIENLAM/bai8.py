
n = int(input("Nhập số phần tử: "))
ds = []
for i in range(n):
    x = int(input("Nhập phần tử: "))
    ds = ds + [x]
print("Danh sách ban đầu:", ds)
for i in range(len(ds)):
    for j in range(i + 1, len(ds)):
        if ds[i] > ds[j]:
            temp = ds[i]
            ds[i] = ds[j]
            ds[j] = temp
print("Sau khi sắp xếp:", ds)
max_val = ds[0]
for x in ds:
    if x > max_val:
        max_val = x

print("Phần tử lớn nhất:", max_val)
min_val = ds[0]
for x in ds:
    if x < min_val:
        min_val = x
print("Phần tử nhỏ nhất:", min_val)
xoa = int(input("Nhập giá trị cần xóa: "))
print("Trước khi xóa:", ds)
found = False
ds_moi = []
for x in ds:
    if x == xoa and not found:
        found = True
        continue
    ds_moi = ds_moi + [x]
print("Sau khi xóa:", ds_moi)