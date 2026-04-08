while True:
    m = int(input())
    n = int(input())
    if 0 < m < n:
        break

ds = []
for i in range(m, n + 1):
    ds.append(i)

tp = tuple(ds)

mid = len(tp) // 2

tp1 = tp[:mid]
tp2 = tp[mid:]

print(tp1)
print(tp2)