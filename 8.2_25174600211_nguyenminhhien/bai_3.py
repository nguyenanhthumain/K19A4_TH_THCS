import random
def la_nt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def tao_ds(n):
    return [random.randint(1, 100) for _ in range(n)]
n = int(input("Nhap n: "))
ds = tao_ds(n)
print("Danh sach:", ds)
print("So nguyen to:")
for i in ds:
    if la_nt(i):
        print(i, end=" ")