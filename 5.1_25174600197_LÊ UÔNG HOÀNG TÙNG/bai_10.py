#bai10
n = int(input("nhap so luong phan tu cua tuple goc: "))
tpl_goc = ()
for i in range(n):
    so = int(input(f"nhap phan tu thu {i+1}: "))
    tpl_goc += (so,)
print("tuple goc:", tpl_goc)
k = int(input("nhap so luong so le can lay (n): "))
so_le = []
for x in tpl_goc:
    if x > 0 and x % 2 == 1:
        so_le.append(x)
    if len(so_le) == k:
        break
tuple_ket_qua = tuple(so_le)
print("tuple chua", k, "so nguyen duong le:", tuple_ket_qua)