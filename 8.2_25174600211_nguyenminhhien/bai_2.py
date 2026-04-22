import random
def tao_ds(n):
    ds = []
    for i in range(n):
        ds.append(random.randint(1, 100))
    return ds
def binh_phuong(ds):
    return list(map(lambda x: x*x, ds))
n = int(input("Nhap n: "))
ds = tao_ds(n)
print("Danh sach:", ds)
print("Binh phuong:", binh_phuong(ds))