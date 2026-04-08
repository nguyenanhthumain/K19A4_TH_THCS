n = int(input("Nhập số lượng phần tử: "))
danh_sach = [0] * n

for i in range(n):
    danh_sach[i] = int(input(f"Nhập phần tử thứ {i}: "))

if n < 2:
    print("Yêu cầu nhập lại")
else:
    gia_tri_lon_thu_nhat = gia_tri_lon_thu_hai = -1
    vi_tri_gia_tri_lon_thu_nhat = vi_tri_gia_tri_lon_thu_hai = -1
    for i in range(n):
        if danh_sach[i] > gia_tri_lon_thu_nhat:
            gia_tri_lon_thu_hai = gia_tri_lon_thu_nhat
            vi_tri_gia_tri_lon_thu_hai = vi_tri_gia_tri_lon_thu_nhat
            gia_tri_lon_thu_nhat = danh_sach[i]
            vi_tri_gia_tri_lon_thu_nhat = i
        elif danh_sach[i] > gia_tri_lon_thu_hai and danh_sach[i] != gia_tri_lon_thu_nhat:
            gia_tri_lon_thu_hai = danh_sach[i]
            vi_tri_gia_tri_lon_thu_hai = i
    if gia_tri_lon_thu_hai != -1:
        print("Phần tử lớn thứ hai:", gia_tri_lon_thu_hai)
        print("Vị trí của phần tử lớn thứ hai:", vi_tri_gia_tri_lon_thu_hai)
    else:
        print("Không có giá trị lớn thứ hai ")

so_duong_lien_tiep_nhieu_nhat = 0
so_luong_hien_tai = 0
for gia_tri in danh_sach:
    if gia_tri > 0:
        so_luong_hien_tai += 1
        if so_luong_hien_tai > so_duong_lien_tiep_nhieu_nhat:
            so_duong_lien_tiep_nhieu_nhat = so_luong_hien_tai
    else:
        so_luong_hien_tai = 0
print("Số lượng số dương liên tiếp nhiều nhất:", so_duong_lien_tiep_nhieu_nhat)

tong_lon_nhat = 0
so_luong_nhieu_nhat = 0
i = 0
while i < n:
    if danh_sach[i] > 0:
        tong_hien_tai = 0
        so_luong_hien_tai = 0
        while i < n and danh_sach[i] > 0:
            tong_hien_tai += danh_sach[i]
            so_luong_hien_tai += 1
            i += 1
        if tong_hien_tai > tong_lon_nhat:
            tong_lon_nhat = tong_hien_tai
            so_luong_nhieu_nhat = so_luong_hien_tai
    else:
        i += 1
print("Số lượng số dương liên tiếp có tổng lớn nhất:", so_luong_nhieu_nhat)