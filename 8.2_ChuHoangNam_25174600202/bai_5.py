#cau5
n = int(input("Nhap do dai n: "))
ds = []
for i in range(n):
    ds.append((i * 12345 + 6789) % 20 + 1)

print("Danh sach:", ds)

ket_qua = list(map(lambda x: x % 2 == 0, ds))
print("Ket qua (True la chan, False la le):", ket_qua)