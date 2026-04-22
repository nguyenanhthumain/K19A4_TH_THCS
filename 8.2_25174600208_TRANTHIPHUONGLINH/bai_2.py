#bai2
import random

def tao_danh_sach(n):
    ds = []
    for i in range(n):
        ds.append(random.randint(1, 100))
    return ds

def binh_phuong(ds):
    f = lambda x: x * x
    kq = []
    for i in ds:
        kq.append(f(i))
    return kq

n = int(input())
a = tao_danh_sach(n)
print(a)
print(binh_phuong(a))