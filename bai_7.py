def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input())
b = int(input())
print(ucln(a, b))
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bcnn(a, b):
    return a * b // ucln(a, b)

a = int(input())
b = int(input())
print(bcnn(a, b))
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def rut_gon(a, b):
    g = ucln(a, b)
    return a//g, b//g

a = int(input())
b = int(input())
tu, mau = rut_gon(a, b)
print(tu, "/", mau)