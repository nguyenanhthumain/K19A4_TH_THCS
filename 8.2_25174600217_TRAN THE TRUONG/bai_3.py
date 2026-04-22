import random
def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def tao_ds_va_loc_nguyen_to(n):
    ds = [random.randint(1, 100) for _ in range(n)]
    so_nt = [x for x in ds if la_so_nguyen_to(x)]
    return ds, so_nt

n = int(input("Nhập số lượng phần tử: "))
ds, nt = tao_ds_va_loc_nguyen_to(n)
print("Danh sách:", ds)
print("Số nguyên tố:", nt)