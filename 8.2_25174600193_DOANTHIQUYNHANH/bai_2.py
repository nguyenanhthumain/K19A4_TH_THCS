import random

def tao_ds_va_binh_phuong(n):
    ds = [random.randint(1, 100) for _ in range(n)]
    print("Ds ban đầu:", ds)

    binh_phuong = list(map(lambda x: x**2, ds))
    print("Ds bình phương:", binh_phuong)


n = int(input("Nhập n: "))
tao_ds_va_binh_phuong(n)