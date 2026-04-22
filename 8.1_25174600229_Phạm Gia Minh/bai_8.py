import math

def hinh_tron(r):
    return 2 * math.pi * r, math.pi * r**2

def hinh_vuong(a):
    return 4 * a, a**2

def hinh_chu_nhat(d, r):
    return 2 * (d + r), d * r

def hinh_tam_giac(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        cv = a + b + c
        p = cv / 2
        dt = math.sqrt(p * (p-a) * (p-b) * (p-c))
        return cv, dt
    return None, None