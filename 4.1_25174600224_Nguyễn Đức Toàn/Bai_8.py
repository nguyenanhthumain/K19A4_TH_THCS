for n in range(2, 1001):
    so_nguyen_to = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            so_nguyen_to = False
            break
    if so_nguyen_to:
        print(n)