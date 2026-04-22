import random
def tao_ds_binh_phuong(n):
    ds = [random.randint(1, 100) for _ in range(n)]
    binh_phuong = list(map(lambda x: x * x, ds))
    return ds, binh_phuong

n = int(input("Nhập số lượng phần tử: "))
ds, bp = tao_ds_binh_phuong(n)
print("Danh sách:", ds)
print("Bình phương:", bp)