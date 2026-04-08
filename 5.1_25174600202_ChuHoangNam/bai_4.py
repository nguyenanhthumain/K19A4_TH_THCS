#cau4
m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
danh_sach = []
so_hien_tai = m
while so_hien_tai <= n and len(danh_sach) < 100:
    danh_sach.append(so_hien_tai)
    so_hien_tai = so_hien_tai + 2
tong = 0
for so in danh_sach:
    tong = tong + so
print("Danh sách:", danh_sach)
print("Tổng là:", tong)