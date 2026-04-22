import random

def bai_2():
    n = int(input())
    ds = [random.randint(1, 100) for _ in range(n)]
    binh_phuong = lambda x: x**2
    kq = [binh_phuong(x) for x in ds]
    print(ds)
    print(kq)

if __name__ == "__main__":
