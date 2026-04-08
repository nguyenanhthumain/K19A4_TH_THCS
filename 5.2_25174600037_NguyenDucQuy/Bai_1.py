n = int(input("Nhập số lượng phần tử n: "))
danh_sach = []
for i in range(n):
    gia_tri = int(input(f"Nhập phần tử thứ {i}: "))
    danh_sach.append(gia_tri)

tong_tat_ca = sum(danh_sach)
print(f"Tổng các phần tử: {tong_tat_ca}")
cac_so_duong = [x for x in danh_sach if x > 0]
print(f"Số lượng số dương: {len(cac_so_duong)}")
print(f"Tổng các số dương: {sum(cac_so_duong)}")
vi_tri_am_dau = -1
for i in range(len(danh_sach)):
    if danh_sach[i] < 0:
        vi_tri_am_dau = i
        break
print(f"Vị trí âm đầu tiên: {vi_tri_am_dau}")
vi_tri_duong_cuoi = -1
for i in range(len(danh_sach)-1, -1, -1):
    if danh_sach[i] > 0:
        vi_tri_duong_cuoi = i
        break
print(f"Vị trí dương cuối cùng: {vi_tri_duong_cuoi}")
if danh_sach:
    so_lon_nhat = max(danh_sach)
    vi_tri_max_cuoi = -1
    for i in range(len(danh_sach)):
        if danh_sach[i] == so_lon_nhat:
            vi_tri_max_cuoi = i
    print(f"Số lớn nhất là {so_lon_nhat}, vị trí cuối cùng là {vi_tri_max_cuoi}")