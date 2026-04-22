from functools import reduce
def cau_a():
    ds = list(filter(lambda x: x % 2 == 0, range(1,101)))
    print("so chan 1-100:", ds)
def cau_b():
    n = int(input("nhap n: "))
    ds = list(range(1, n+1))
    so_chan = list(filter(lambda x: x % 2 == 0, ds))
    tong = reduce(lambda x, y: x + y, so_chan, 0)
    print("tong so chan:", tong)
def bai_15():
    cau_a()
    cau_b()
bai_15()