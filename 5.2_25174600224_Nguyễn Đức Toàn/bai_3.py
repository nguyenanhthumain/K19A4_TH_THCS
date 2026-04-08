danh_sach = []
while True:
    x = int(input("Nhập số: "))
    if x == 0:
        break
    danh_sach = danh_sach + [x]  

danh_sach = [x for x in danh_sach if x > 0] + [x for x in danh_sach if x <= 0]

print("Danh sách sau khi chuyển số dương lên đầu:", danh_sach)

m = int(input("Nhập số m để chèn: "))

danh_sach = [m] + danh_sach + [m]

if len(danh_sach) >= 5:
    danh_sach = danh_sach[:4] + [m] + danh_sach[4:]

print("Danh sách cuối cùng:", danh_sach)