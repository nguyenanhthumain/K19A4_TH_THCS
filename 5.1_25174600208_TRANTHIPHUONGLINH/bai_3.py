while True:
    m = int(input())
    n = int(input())
    if m > 0 and m < n:
        break
a = []
for i in range(m, n+1):
    a.append(i)

def f(x):
    if x % 2 == 0:
        return True
    else:
        return False

b = list(filter(f, a))

print(b)