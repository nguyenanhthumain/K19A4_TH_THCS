n = int(input("Nhập n: "))
a = [int(input(f"Nhập a[{i}]: ")) for i in range(n)]
tap_hop_so = list(set(a))
if len(tap_hop_so) < 2:
    print("Không có số lớn thứ hai.")
else:
    tap_hop_so.sort()
    so_lon_thu_hai = tap_hop_so[-2]
    vi_tri_so_hai = [i for i, x in enumerate(a) if x == so_lon_thu_hai]
    print(f"Số lớn thứ hai là {so_lon_thu_hai} tại các vị trí {vi_tri_so_hai}")
so_luong_max = 0
tong_max = 0
dem_hien_tai = 0
tong_hien_tai = 0
for x in a:
    if x > 0:
        dem_hien_tai += 1
        tong_hien_tai += x
    else:
        if dem_hien_tai > so_luong_max:
            so_luong_max = dem_hien_tai
        if tong_hien_tai > tong_max:
            tong_max = tong_hien_tai
        dem_hien_tai = 0
        tong_hien_tai = 0
so_luong_max = max(so_luong_max, dem_hien_tai)
tong_max = max(tong_max, tong_hien_tai)
print(f"Số lượng số dương liên tiếp nhiều nhất: {so_luong_max}")
print(f"Tổng dãy số dương liên tiếp lớn nhất: {tong_max}")