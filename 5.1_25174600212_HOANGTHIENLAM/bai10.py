n = int(input())
ds = []
for i in range(n):
    x = int(input())
    ds.append(x)
tp = tuple(ds)
k = int(input())
k = k % len(tp)
tp_moi = tp[-k:] + tp[:-k]
print(tp_moi)