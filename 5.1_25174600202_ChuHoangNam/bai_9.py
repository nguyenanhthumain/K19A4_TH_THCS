#bai9
m = int(input("Nhap m: "))
n = int(input("Nhap n (n > m): "))
L_tam = []
for i in range(m, n + 1):
    L_tam.append(i)
t = tuple(L_tam)
diem_giua = len(t) // 2
tp1 = t[:diem_giua]
tp2 = t[diem_giua:]

print("Tuple goc:", t)
print("tp1 (nua dau):", tp1)
print("tp2 (nua cuoi):", tp2)