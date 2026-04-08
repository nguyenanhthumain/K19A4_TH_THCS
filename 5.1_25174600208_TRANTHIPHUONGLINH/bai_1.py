n = int(input())
m = int(input())
ds = []
for i in range(1, n+1):
    ds.append(i*i)
if m >= n:
    print(ds)
else:
    print(ds[:m])