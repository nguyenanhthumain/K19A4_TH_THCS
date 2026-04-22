import random

def bai_5():
    n = int(input())
    ds = [random.randint(1, 100) for _ in range(n)]
    kiem_tra_chan = lambda x: x % 2 == 0
    kq = [kiem_tra_chan(x) for x in ds]
    print(ds)
    print(kq)

if __name__ == "__main__":
    