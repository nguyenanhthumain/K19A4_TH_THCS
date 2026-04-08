#cau10
n = int(input("Nhap so luong phan tu n cho Tuple: "))
L_nhap = []
for i in range(n):
    so = int(input(f"Nhap phan tu thu {i+1}: "))
    L_nhap.append(so)
t_goc = tuple(L_nhap)
L_le = []
for x in t_goc:
    if x > 0 and x % 2 != 0:
        L_le.append(x)

t_ket_qua = tuple(L_le)
print("Tuple cac so nguyen duong le:", t_ket_qua)