def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def a ():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    print("UCLN =", ucln(a, b))
a()

def bcnn(a, b):
    return (a * b) // ucln(a, b)
def b():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    print("BCNN =", bcnn(a, b))
b()


def rut_gon(tu, mau):
    g = ucln(tu, mau)
    tu = tu // g
    mau = mau // g
    return tu, mau
def c():
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
    if mau == 0:
        print("Yêu cầu nhập lại")
        return
    
    tu_moi, mau_moi = rut_gon(tu, mau)
    print("Phân số rút gọn:", tu_moi, "/", mau_moi)
c()


def d():
    n = int(input("Nhập số nguyên n: "))
    if n <= 0:
        print("Yêu cầu nhập lại")
        return
    x = int(input("Nhập số thứ 1: "))
    so_nho_nhat = x
    so_lon_nhat = x
    
    for i in range(2, n + 1):
        x = int(input("Nhập số thứ " + str(i) + ": "))
        if x < so_nho_nhat:
            so_nho_nhat = x
        if x > so_lon_nhat:
            so_lon_nhat = x
    print("Số nhỏ nhất =", so_nho_nhat)
    print("Số lớn nhất =", so_lon_nhat)
d()