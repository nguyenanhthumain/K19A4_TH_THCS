n = int(input())
a = []
for i in range(1,n+1):
    a.append(i)
nt = []
hh = []
for i in a:
    dem = 0
    for j in range(1,i+1):
        if i % j == 0:
            dem = dem + 1
    if dem == 2:
        nt.append(i)
for i in a:
    s = 0
    for j in range(1,i):
        if i % j == 0:
            s = s + j
    if s == i:
        hh.append(i)
print(nt)
print(hh)