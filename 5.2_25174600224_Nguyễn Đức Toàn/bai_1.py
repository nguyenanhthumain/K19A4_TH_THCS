n = int(input("Nhập số lượng phần tử: "))
danh_sach = [0] * n  
for i in range(n):
    danh_sach[i] = int(input(f"Nhập phần tử thứ {i}: "))

tong = 0
for gia_tri in danh_sach:
    tong += gia_tri
print("Tổng các phần tử:", tong)

so_hang_duong = 0
tong_so_hang_duong = 0
for gia_tri in danh_sach:
    if gia_tri > 0:
        so_hang_duong += 1
        tong_so_hang_duong += gia_tri
print("Số lượng số dương:", so_hang_duong)
print("Tổng các số dương:", tong_so_hang_duong)

vi_tri_am_dau_tien = -1
for i in range(n):
    if danh_sach[i] < 0:
        vi_tri_am_dau_tien = i
        break
if vi_tri_am_dau_tien != -1:
    print("Vị trí phần tử âm đầu tiên:", vi_tri_am_dau_tien)
else:
    print("Không có phần tử âm trong danh sách")

vi_tri_duong_cuoi_cung = -1
for i in range(n-1, -1, -1):
    if danh_sach[i] > 0:
        vi_tri_duong_cuoi_cung = i
        break
if vi_tri_duong_cuoi_cung != -1:
    print("Vị trí phần tử dương cuối cùng:", vi_tri_duong_cuoi_cung)
else:
    print("Không có phần tử dương trong danh sách")

gia_tri_lon_nhat = danh_sach[0]
vi_tri_cuoi_cung = 0
for i in range(n):
    if danh_sach[i] >= gia_tri_lon_nhat:
        gia_tri_lon_nhat = danh_sach[i]
        vi_tri_cuoi_cung = i
print("Phần tử lớn nhất:", gia_tri_lon_nhat)
print("Vị trí phần tử lớn nhất cuối cùng:", vi_tri_cuoi_cung)