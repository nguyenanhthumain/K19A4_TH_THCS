while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    
    if 0 < m < n:
        break
    else:
        print("Yêu cầu nhập lại: ")

danh_sach = [0] * 100
so_tu_nhien = m
i = 0

while i < 100 and so_tu_nhien <= n:
    danh_sach[i] = so_tu_nhien
    so_tu_nhien += 2
    i += 1
danh_sach = danh_sach[:i]
tong = 0
for so_tu_nhien in danh_sach:
    tong += so_tu_nhien

print("Danh sách:", danh_sach)
print("Tổng:", tong)