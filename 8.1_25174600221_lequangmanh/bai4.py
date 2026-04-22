def bai4():
    n = int(input("Nhập n: "))
    x = int(input("Nhập x: "))
    y = int(input("Nhập y: "))

    # a
    P = 1
    for i in range(n+1):
        P *= (2*i+1)
    print("P(n):", P)

    # b
    S1 = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            S1 -= i
        else:
            S1 += i
    print("S1:", S1)

    # c
    S2 = 0
    for i in range(1, n+1):
        tong = 0
        for j in range(1, i+1):
            tong += j
        S2 += tong
    print("S2:", S2)

    # d
    tong = 0
    for k in range(1, n+1):
        tong += (x + 3*y + k)
    print("P(x,y):", x**y + tong)

bai4()