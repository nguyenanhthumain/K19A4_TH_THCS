# Cách 1 while:
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
gcd = ucln(a, b)
bcnn = abs(a * b) // gcd
print("UCLN =", gcd)
print("BCNN =", bcnn)
# Cách 2 for:
def ucln(a, b):
    for _ in range(max(a, b)):
        if b == 0:
            break
        a, b = b, a % b
    return a
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
gcd = ucln(a, b)
bcnn = abs(a * b) // gcd
print("UCLN =", gcd)
print("BCNN =", bcnn)
