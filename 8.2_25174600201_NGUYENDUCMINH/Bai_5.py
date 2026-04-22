import random

def kiem_tra_chan(n):
    ds = [random.randint(1, 100) for _ in range(n)]
    chan = list(map(lambda x: x % 2 == 0, ds))
    return ds, chan