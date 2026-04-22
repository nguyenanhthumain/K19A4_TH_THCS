import random
def tao_ds(n):
    return [random.randint(1, 100) for _ in range(n)]
def kiem_tra(ds):
    return list(map(lambda x: True if x % 2 == 0 else False, ds)) 
n = int(input("Nhap n: "))
ds = tao_ds(n)
print("Danh sach:", ds)
print("Chan/Le:", kiem_tra(ds))