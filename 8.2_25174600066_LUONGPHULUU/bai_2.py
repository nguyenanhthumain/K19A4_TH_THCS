import random
def tao_danh_sach(n):
    danh_sach = [random.randint(1, 10) for _ in range(n)]
    binh_phuong = list(map(lambda x: x**2, danh_sach))
    return danh_sach, binh_phuong

n = int(input("Nhập số phần tử n: "))
ds, ds_bp = tao_danh_sach(n)
print("Danh sách ban đầu:", ds)
print("Danh sách bình phương:", ds_bp)