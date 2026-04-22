def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def bcnn(a, b):
    return a * b // ucln(a, b)
def rut_gon(tu, mau):
    g = ucln(tu, mau)
    return tu//g, mau//g
def min_max():
    n = int(input("nhap so luong: "))
    ds = []
    for i in range(n):
        ds.append(int(input("nhap so: ")))
    print("min =", min(ds))
    print("max =", max(ds))
def bai_7():
    a = int(input("nhap a: "))
    b = int(input("nhap b: "))
    print("ucln =", ucln(a,b))
    print("bcnn =", bcnn(a,b))
    tu = int(input("tu so: "))
    mau = int(input("mau so: "))
    tu, mau = rut_gon(tu, mau)
    print("phan so rut gon:", tu, "/", mau)
    min_max()
bai_7()