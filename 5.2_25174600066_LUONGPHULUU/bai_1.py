n = int(input("Nhập số phần tử: "))
a = []
i = 0
while i < n:
    x = int(input(f"Nhập phần tử thứ {i}: "))
    a.append(x)
    i += 1
# a:
tong = 0
i = 0
while i < n:
    tong += a[i]
    i += 1
print("Tổng các phần tử:", tong)
# b:
dem_duong = 0
tong_duong = 0
i = 0
while i < n:
    if a[i] > 0:
        dem_duong += 1
        tong_duong += a[i]
    i += 1
print("Số lượng số dương:", dem_duong)
print("Tổng các số dương:", tong_duong)
# c:
vi_tri_am_dau = -1
i = 0
while i < n:
    if a[i] < 0:
        vi_tri_am_dau = i
        break
    i += 1
print("Vị trí phần tử âm đầu tiên:", vi_tri_am_dau)
# d:
vi_tri_duong_cuoi = -1
i = n - 1
while i >= 0:
    if a[i] > 0:
        vi_tri_duong_cuoi = i
        break
    i -= 1
print("Vị trí phần tử dương cuối cùng:", vi_tri_duong_cuoi)
# e:
max_value = a[0]

i = 1
while i < n:
    if a[i] > max_value:
        max_value = a[i]
    i += 1
vi_tri_max_cuoi = -1
i = 0
while i < n:
    if a[i] == max_value:
        vi_tri_max_cuoi = i
    i += 1
print("Phần tử lớn nhất:", max_value)
print("Vị trí cuối cùng của max:", vi_tri_max_cuoi)