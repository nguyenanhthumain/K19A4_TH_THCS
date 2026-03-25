for n in range(2, 1001):
    la_snt = True
    for m in range(2, int(n ** 0.5) + 1):
        if n % m == 0:
            la_snt = False
            break
    if la_snt:
        print(n, end=" ")