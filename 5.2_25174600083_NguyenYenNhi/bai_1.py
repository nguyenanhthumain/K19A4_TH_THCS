#bai_1
"""
Cho danh sách a có độ dài là n với các phần tử là số tự nhiên chứa cả giá trị âm và
dương được nhập từ bàn phím. Yêu cầu:
a. Viết chương trình tính tổng các phần tử của danh sách.
b. Viết chương trình đếm số lượng các số hạng dương và tổng của các số hạng
dương.
c. Tìm vị trí của phần tử âm đầu tiên trong danh sách.
d. Tìm vị trí của phần tử dương cuối cùng trong danh sách.
e. Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng.
"""

n = int(input("Nhập độ dài của danh sách: "))
a = []
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i + 1}: "))
    a.append(phan_tu)

#a
tong = 0 
for phan_tu in a:
    tong += phan_tu
print(f"Tổng các phần tử của danh sách: {tong}")

#b
so_hang_duong = 0
tong_duong = 0
for phan_tu in a:
    if phan_tu > 0:
        so_hang_duong += 1
        tong_duong += phan_tu
print(f"Số lượng các số hạng dương: {so_hang_duong}")
print(f"Tổng của các số hạng dương: {tong_duong}")

#c
vi_tri_am_dau_tien = -1
for i in range(n):
    if a[i] < 0:
        vi_tri_am_dau_tien = i
        break   
if vi_tri_am_dau_tien != -1:
    print(f"Vị trí của phần tử âm đầu tiên trong danh sách: {vi_tri_am_dau_tien}")      

#d
vi_tri_duong_cuoi_cung = -1
for i in range(n - 1, -1, -1):
    if a[i] > 0:
        vi_tri_duong_cuoi_cung = i
        break
if vi_tri_duong_cuoi_cung != -1:
    print(f"Vị trí của phần tử dương cuối cùng trong danh sách: {vi_tri_duong_cuoi_cung}")

#e
phan_tu_lon_nhat = a[0]
vi_tri_lon_nhat_cuoi_cung = 0
for i in range(1, n):
    if a[i] >= phan_tu_lon_nhat:
        phan_tu_lon_nhat = a[i]
        vi_tri_lon_nhat_cuoi_cung = i
print(f"Phần tử lớn nhất của danh sách: {phan_tu_lon_nhat}")
print(f"Vị trí của phần tử lớn nhất cuối cùng: {vi_tri_lon_nhat_cuoi_cung}")