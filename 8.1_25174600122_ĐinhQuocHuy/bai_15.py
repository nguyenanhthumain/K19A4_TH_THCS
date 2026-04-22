arr = [i for i in range(1, 101) if i % 2 == 0]
print(arr)
from functools import reduce

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

chan = list(filter(lambda x: x % 2 == 0, arr))
tong = reduce(lambda a, b: a + b, chan, 0)

print(tong)