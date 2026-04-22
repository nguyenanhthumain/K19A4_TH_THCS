from functools import reduce
ds_chan = [i for i in range(1, 101) if i % 2 == 0]
print("So chan 1-100:", ds_chan)
n = int(input("Nhap n: "))
ds = list(range(1, n+1))
chan = list(filter(lambda x: x % 2 == 0, ds))
tong = reduce(lambda a, b: a + b, chan)
print("Danh sach:", ds)
print("So chan:", chan)
print("Tong so chan:", tong)