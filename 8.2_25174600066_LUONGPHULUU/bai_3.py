import random
def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def tao_danh_sach(n):
    danh_sach = [random.randint(1, 50) for _ in range(n)]
    print("Danh sách ban đầu:", danh_sach)
    print("Các số nguyên tố trong danh sách:")
    for so in danh_sach:
        if la_so_nguyen_to(so):
            print(so, end=" ")

n = int(input("Nhập số phần tử n: "))
tao_danh_sach(n)