#cau2
n = int(input("Nhap do dai n: "))
ds = []
for i in range(n):
    ds.append((i * 12345 + 6789) % 10 + 1)

print("Danh sach goc:", ds)
ket_qua = list(map(lambda x: x * x, ds))
print("Danh sach binh phuong:", ket_qua)