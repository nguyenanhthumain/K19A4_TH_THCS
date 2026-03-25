for n in range(1, 1001):
    if n < 2:
        continue
    ok = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            ok = False
            break
    if ok:
        print(n, end=" ")