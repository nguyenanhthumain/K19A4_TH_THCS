#câu a
def P(n):
    tich = 1
    for i in range(n + 1):
        tich *= (2 * i + 1)
    return tich


n = int(input("Nhập n: "))
print("P(n) =", P(n))

#câu b
def S(n):
    tong = 0
    for i in range(1, n + 1):
        tong += ((-1) ** (i + 1)) * i
    return tong


n = int(input("Nhập n: "))
print("S(n) =", S(n))

#câu c
def S(n):
    tong = 0
    for i in range(1, n + 1):
        tong += sum(range(1, i + 1))
    return tong


n = int(input("Nhập n: "))
print("S(n) =", S(n))

#câu d
def P(x, y, n):
    tong = 0
    for k in range(1, n + 1):
        tong += (x + 3 ** (2 * y) + y ** k)
    return x ** y + tong


x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
n = int(input("Nhập n (>1): "))

print("P(x, y) =", P(x, y, n))
