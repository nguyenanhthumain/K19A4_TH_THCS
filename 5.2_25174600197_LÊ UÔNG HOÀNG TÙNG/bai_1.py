#bai1
n = int(input("nhap do dai danh sach n: "))
a = []
for i in range(n):
    so = int(input(f"nhap phan tu thu {i+1}: "))
    a.append(so)
print("danh sach a:", a)
print("tong cac phan tu:", sum(a))
dem_duong = 0
tong_duong = 0
for x in a:
    if x > 0:
        dem_duong += 1
        tong_duong += x
print("so luong so duong:", dem_duong)
print("tong so duong:", tong_duong)
for i in range(len(a)):
    if a[i] < 0:
        print("vi tri phan tu am dau tien:", i)
        break
else:
    print("khong co phan tu am")
vitri_duong_cuoi = -1
for i in range(len(a)):
    if a[i] > 0:
        vitri_duong_cuoi = i
if vitri_duong_cuoi != -1:
    print("vi tri phan tu duong cuoi cung:", vitri_duong_cuoi)
else:
    print("khong co phan tu duong")
if a:
    max_val = max(a)
    vitri_max_cuoi = len(a) - 1 - a[::-1].index(max_val)
    print("phan tu lon nhat:", max_val)
    print("vi tri phan tu lon nhat cuoi cung:", vitri_max_cuoi)