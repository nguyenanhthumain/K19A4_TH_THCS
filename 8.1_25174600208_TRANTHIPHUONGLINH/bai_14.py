# Bai 14
def tao_ds(n):
    kq = []
    for i in range(n):
        so = int(input("Nhap: "))
        kq = kq + [so]   # khác append
    return kq

def binh_phuong(ds):
    return list(map(lambda x: x*x, ds))

n = int(input("Nhap n: "))
ds = tao_ds(n)

print("Binh phuong:", binh_phuong(ds))