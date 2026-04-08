n = int(input())
t = ()
i = 1
while True:
    if i % 2 != 0:
        t = t + (i,)
    if len(t) == n:
        break
    i = i + 1
print(t)