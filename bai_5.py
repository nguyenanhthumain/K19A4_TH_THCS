n = int(input("Nhập n: "))
lst = list(range(1, n+1))
prime = []
for x in lst:
    if x < 2:
        continue
    ok = True
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            ok = False
            break
    if ok:
        prime.append(x)
perfect = []
for x in lst:
    s = sum(i for i in range(1, x) if x % i == 0)
    if s == x:
        perfect.append(x)
print("Nguyên tố:", prime)
print("Hoàn hảo:", perfect)