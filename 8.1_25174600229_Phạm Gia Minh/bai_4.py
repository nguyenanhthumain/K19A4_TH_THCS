#cau a
def P(n):
    tich = 1

    for i in range(0, n + 1):
        tich = tich * (2 * i + 1)

    return tich

n = int(input("Nhập n: "))
print("P(n) =", P(n))

#cau b
def S(n):
    tong = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            tong = tong - i
        else:
            tong = tong + i

    return tong

n = int(input("Nhập n: "))
print("S(n) =", S(n))

#cau c
def S(n):
    tong = 0

    for i in range(1, n + 1):
        tong_con = 0

        for j in range(1, i + 1):
            tong_con = tong_con + j

        tong = tong + tong_con

    return tong

n = int(input("Nhập n: "))
print("S(n) =", S(n))

# cau d
def mu(a, b):
    ket_qua = 1

    for i in range(b):
        ket_qua = ket_qua * a

    return ket_qua

def P(x, y, n):
    tong = 0

    for k in range(1, n + 1):
        tong = tong + (x + 32 * y + mu(y, k))

    return mu(x, y) + tong

x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
n = int(input("Nhập n: "))

print("P(x,y) =", P(x, y, n))