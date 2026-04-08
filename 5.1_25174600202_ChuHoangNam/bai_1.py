#cau1
n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
ds_binh_phuong = []
for i in range(1, n + 1):
    ds_binh_phuong.append(i * i)
if m > n:
    m = n
ket_qua_list = []
for i in range(m):
    ket_qua_list.append(ds_binh_phuong[i])
ket_qua_cuoi_cung = tuple(ket_qua_list)

print("Kết quả (dạng Tuple):", ket_qua_cuoi_cung)