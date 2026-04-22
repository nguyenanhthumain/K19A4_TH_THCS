def phep_tinh(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    if b != 0: print(f"{a} / {b} = {a / b}")

def tinh_luy_thua_phuc_tap(a, n, b):
    print(f"a^(b+n) = {a**(b+n)}")
    print(f"b^(n+2a) = {b**(n+2*a)}")

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
n = float(input("Nhập n: "))
phep_tinh(a, b)
tinh_luy_thua_phuc_tap(a, n, b)