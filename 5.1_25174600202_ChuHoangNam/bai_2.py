#cau2
n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
danh_sach_binh_phuong = []
for i in range(1, n + 1):
    gia_tri_binh_phuong = i * i
    danh_sach_binh_phuong.append(gia_tri_binh_phuong)
danh_sach_ket_qua = []
for i in range(m, n):
    gia_tri = danh_sach_binh_phuong[i]
    danh_sach_ket_qua.append(gia_tri)
ket_qua_cuoi_cung = tuple(danh_sach_ket_qua)
print(ket_qua_cuoi_cung)