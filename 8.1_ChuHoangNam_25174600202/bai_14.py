#cau14
n = int(input("Nhap so luong phan tu n: "))
ds = []

for i in range(n):
    so = int(input(f"Nhap phan tu thu {i+1}: "))
    ds.append(so)

list_binh_phuong = list(map(lambda x: x*x, ds))

print("List ban dau:", ds)
print("List binh phuong:", list_binh_phuong)