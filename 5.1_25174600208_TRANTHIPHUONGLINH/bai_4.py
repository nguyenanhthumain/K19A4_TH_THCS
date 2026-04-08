m = int(input())
n = int(input())
a = []
i = m
while i <= n and len(a) < 100:
    a.append(i)
    i = i + 2
tong = 0
for x in a:
    tong = tong + x
print(tong)