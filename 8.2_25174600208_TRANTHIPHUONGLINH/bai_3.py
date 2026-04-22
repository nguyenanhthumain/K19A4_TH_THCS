#bai3
import random

def la_snt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())
ds = []
for i in range(n):
    ds.append(random.randint(1, 100))

print(ds)
for x in ds:
    if la_snt(x):
        print(x, end=" ")