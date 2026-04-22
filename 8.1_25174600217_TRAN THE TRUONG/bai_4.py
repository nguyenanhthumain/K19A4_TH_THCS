#a.
def tinh_P():
    n = int(input("Nhập n (n >= 0): "))
    P = 1
    for i in range(0, n + 1):
        P *= (2 * i + 1)
    print("P(n) =", P)

#b.
def tinh_S_dau_tru():
    n = int(input("Nhập n (n >= 0): "))
    S = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            S -= i
        else:
            S += i
    print("S(n) =", S)

#c.
def tinh_S_tong_luy_tien():
    n = int(input("Nhập n: "))
    S = 0
    tong_con = 0
    for i in range(1, n + 1):
        tong_con += i
        S += tong_con
    print("S(n) =", S)

#d.
def luy_thua(x, y):
    kq = 1
    for i in range(y):
        kq *= x
    return kq
def tinh_P_xy():
    x = int(input("Nhập x: "))
    y = int(input("Nhập y: "))
    n = int(input("Nhập n (n > 1): "))

    P = luy_thua(x, y)

    for k in range(1, n + 1):
        P += (x + 32 * y + luy_thua(y, k))

    print("P(x, y) =", P)


def main():
    print("a.")
    tinh_P()

    print("\nb.")
    tinh_S_dau_tru()

    print("\nc.")
    tinh_S_tong_luy_tien()

    print("\nd.")
    tinh_P_xy()


main()