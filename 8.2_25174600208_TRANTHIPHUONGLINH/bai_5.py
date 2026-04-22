#bài 5
import random

def tao_ds(n):
    ds = []
    for i in range(n):
        ds.append(random.randint(1, 100))
    return ds

def kiem_tra_chan(ds):
    f = lambda x: x % 2 == 0
    kq = []
    for i in ds:
        kq.append(f(i))
    return kq

n = int(input())
a = tao_ds(n)
print(a)
print(kiem_tra_chan(a))