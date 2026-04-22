def tinh_toan():
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    if b != 0:
        print("a / b =", a / b)
    else:
        print("Lỗi")

def luy_thua():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    n = int(input("Nhập n: "))
    p1 = 1
    for _ in range(b+n):
        p1 *= a
    p2 = 1
    for _ in range(n + 2*a):
        p2 *= b
    print("a^(b+n) =", p1)
    print("b^(n+2a) =", p2)

tinh_toan()
luy_thua()