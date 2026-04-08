#cau10
danh_sach = [i for i in range(201) if i % 5 == 0 and i % 7 == 0]

vi_tri_ngau_nhien = id(danh_sach) % len(danh_sach)

so_chon_duoc = danh_sach[vi_tri_ngau_nhien]

print("Danh sach cac so thoa man:", danh_sach)
print("So ngau nhien chon duoc là:", so_chon_duoc)