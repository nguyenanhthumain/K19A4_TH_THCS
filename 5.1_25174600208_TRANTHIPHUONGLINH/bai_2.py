n = int(input())
m = int(input())

a = []
for i in range(1, n+1):
    a.append(i*i)
if m >= n:
    print([])
else:
    i = m
    while i < n:
        print(a[i], end=" ")
        i = i + 1