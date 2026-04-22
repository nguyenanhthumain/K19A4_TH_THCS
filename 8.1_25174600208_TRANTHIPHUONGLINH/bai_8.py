# Bai 8
def tinh_tron(r):
    cv = 2 * 3.14 * r
    dt = 3.14 * r * r
    return cv, dt

def tinh_vuong(a):
    return 4*a, a*a

def tinh_chu_nhat(d, r):
    return 2*(d+r), d*r

def tinh_tam_giac(a, b, c):
    p = (a + b + c) / 2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    return a+b+c, s

print("=== Bai 8 ===")

cv, dt = tinh_tron(5)
print("Hinh tron:", cv, dt)