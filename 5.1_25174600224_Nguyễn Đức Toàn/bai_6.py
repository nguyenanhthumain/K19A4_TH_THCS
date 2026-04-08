import random

lua_chon = ["bua", "keo", "la"]

so_luot_thang = 0
so_luot_hoa = 0
so_luot_thua = 0

for luot in range(1, 6):
    nguoi_choi = input(f"Lượt {luot} – Chọn 'bua', 'keo' hay 'la': ").lower()
    if nguoi_choi not in lua_chon:
        print("Chọn lại lựa chọn: ")
        continue
    
    may_tinh_choi = random.choice(lua_chon)
    print("Máy tính chọn:", may_tinh_choi)
    
    if nguoi_choi == may_tinh_choi:
        so_luot_hoa += 1
        print("Kết quả: Hòa")
    elif (nguoi_choi == "bua" and may_tinh_choi == "keo") or \
         (nguoi_choi == "keo" and may_tinh_choi == "la") or \
         (nguoi_choi == "la" and may_tinh_choi == "bua"):
        so_luot_thang += 1
        print("Kết quả: Thắng")
    else:
        so_luot_thua += 1
        print("Kết quả: Thua")

print("Số lượt thắng:", so_luot_thang)
print("Số lượt hòa:", so_luot_hoa)
print("Số lượt thua:", so_luot_thua)