#cau1
n = int(input("Nhap do dai n cua danh sach: "))
a = []
for i in range(n):
    a.append(int(input(f"Nhap phan tu thu {i}: ")))
tong_tat_ca = 0
for x in a:
    tong_tat_ca += x
dem_duong = 0
tong_duong = 0
for x in a:
    if x > 0:
        dem_duong += 1
        tong_duong += x
vi_tri_am_dau = -1 
for i in range(len(a)):
    if a[i] < 0:
        vi_tri_am_dau = i
        break 
vi_tri_duong_cuoi = -1
for i in range(len(a)):
    if a[i] > 0:
        vi_tri_duong_cuoi = i 
so_lon_nhat = a[0]
vi_tri_lon_nhat_cuoi = 0
for i in range(len(a)):
    if a[i] >= so_lon_nhat:
        so_lon_nhat = a[i]
        vi_tri_lon_nhat_cuoi = i

print(f"Tong: {tong_tat_ca}")
print(f"So luong so duong: {dem_duong}, Tong duong: {tong_duong}")
print(f"Vi tri am dau tien: {vi_tri_am_dau}")
print(f"Vi tri dương cuoi cung: {vi_tri_duong_cuoi}")
print(f"Lon nhat: {so_lon_nhat}, Vị trí cuối: {vi_tri_lon_nhat_cuoi}")