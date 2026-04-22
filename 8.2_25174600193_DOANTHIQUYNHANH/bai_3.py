import random

def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def in_so_nguyen_to(n):
    ds = [random.randint(1, 100) for _ in range(n)]
    print("Danh sách:", ds)

    so_nguyen_to = [x for x in ds if la_so_nguyen_to(x)]
    print("Các số nguyên tố:", so_nguyen_to)


n = int(input("Nhập n: "))
in_so_nguyen_to(n)