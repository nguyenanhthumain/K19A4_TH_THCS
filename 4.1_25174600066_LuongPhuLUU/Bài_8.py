for n in range(2, 1001):
    la_snt = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            la_snt = False
            break
        i += 1
    if la_snt:
        print(n, end=" ")