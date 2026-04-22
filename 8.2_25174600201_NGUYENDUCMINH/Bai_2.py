import random

def tao_danh_sach_binh_phuong(n):
    ds = [random.randint(1, 100) for _ in range(n)]
    binh_phuong = list(map(lambda x: x**2, ds))
    return ds, binh_phuong