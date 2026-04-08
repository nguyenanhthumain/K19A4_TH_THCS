danh_sach = []
while True:
    so = int(input("Nhập số (0 để dừng): "))
    if so == 0: break
    danh_sach.append(so)
ds_chen = [1, 2, 3]
danh_sach = ds_chen + danh_sach             
danh_sach = danh_sach + ds_chen             
if len(danh_sach) >= 5:
    danh_sach[4:4] = ds_chen                
print(f"Sau khi chèn: {danh_sach}")
k = int(input("Nhập vị trí k cần xóa (bắt đầu từ 1): "))
if 1 <= k <= len(danh_sach):
    danh_sach.pop(k-1)
print(f"Sau khi xóa vị trí {k}: {danh_sach}")
danh_sach.sort()
print(f"Tăng dần: {danh_sach}")
danh_sach.sort(reverse=True)
print(f"Giảm dần: {danh_sach}")