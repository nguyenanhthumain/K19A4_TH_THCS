def P(n):
    tich = 1
    for i in range(n + 1):
        tich *= (2 * i + 1)
    return tich
def a():
    n = int(input("Nhập n: "))
    print("P(n) =", P(n))
a()

def S(n):
    tong = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            tong -= i
        else:
            tong += i
    return tong
def b():
    n = int(input("Nhập n: "))
    print("S(n) =", S(n))
b()


def S_2(n):
    tong = 0
    tam = 0
    for i in range(1, n + 1):
        tam += i
        tong += tam
    return tong
def c():
    n = int(input("Nhập n: "))
    print("S(n) =", S_2(n))
c()


def P_xy(x, y, n):
    tong = 0
    lt = 1
    for i in range(y):
        lt *= x
    tong += lt
    
    for k in range(1, n + 1):
        mu = 1
        for i in range(k):
            mu *= y
        tong += (x + 32 * y + mu)
    return tong

def d():
    x = int(input("Nhập x: "))
    y = int(input("Nhập y: "))
    n = int(input("Nhập n: "))
    
    if n <= 1:
        print("Yêu cầu nhập lại")
        return
    print("P(x,y) =", P_xy(x, y, n))
d()