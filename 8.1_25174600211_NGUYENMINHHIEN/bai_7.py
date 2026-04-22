def ucln(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
def bcnn(a, b):
    return abs(a*b)//ucln(a,b) if a and b else 0
def rut_gon(tu, mau):
    if mau == 0:
        print("Mau = 0")
        return
    g = ucln(tu, mau)
    print("Rut gon:", tu//g, "/", mau//g)
def min_max():
    n = int(input("n: "))
    ds = [int(input()) for _ in range(n)]
    print("min:", min(ds))
    print("max:", max(ds))
a = int(input("a: "))
b = int(input("b: "))
print("ucln:", ucln(a,b))
print("ucln:", bcnn(a,b))
tu = int(input("Tu: "))
mau = int(input("Mau: "))
rut_gon(tu, mau)
min_max()