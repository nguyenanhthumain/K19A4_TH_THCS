n = int(input("Nhập số lượng phần tử n: "))
a = []
for i in range(n):
    x = int(input(f"Nhập phần tử a[{i}]: "))
    a.append(x)

print("Danh sách vừa nhập:", a)

#a.
tong = sum(a)
print("a. Tổng các phần tử của danh sách =", tong)

#b.
so_duong = [x for x in a if x > 0]
dem_duong = len(so_duong)
tong_duong = sum(so_duong)

print("b. Số lượng số dương =", dem_duong)
print("   Tổng các số dương =", tong_duong)

#c.
vi_tri_am_dau = -1
for i in range(n):
    if a[i] < 0:
        vi_tri_am_dau = i
        break

print("c. Vị trí phần tử âm đầu tiên =", vi_tri_am_dau)

#d.
vi_tri_duong_cuoi = -1
for i in range(n - 1, -1, -1):
    if a[i] > 0:
        vi_tri_duong_cuoi = i
        break

print("d. Vị trí phần tử dương cuối cùng =", vi_tri_duong_cuoi)

#e.
max_val = max(a)
vi_tri_max_cuoi = len(a) - 1 - a[::-1].index(max_val)

print("e. Phần tử lớn nhất =", max_val)
print("   Vị trí xuất hiện cuối cùng của phần tử lớn nhất =", vi_tri_max_cuoi)