import random

danh_sach_A = []
while len(danh_sach_A) < 1000:
    so_ngau_nhien = random.randint(1, 99999)
    if so_ngau_nhien % 7 != 0:
        danh_sach_A.append(so_ngau_nhien)

print(f"Đã sinh {len(danh_sach_A)} số thỏa mãn điều kiện.")
print("5 số đầu tiên:", danh_sach_A[:5])