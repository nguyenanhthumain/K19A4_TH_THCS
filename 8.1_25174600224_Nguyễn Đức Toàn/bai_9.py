def cong(a, b):
    return a + b
def tru(a, b):
    return a - b
def nhan(a, b):
    return a * b
def chia(a, b):
    if b == 0:
        return "Không chia được cho 0"
    return a / b
def a():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    print("Tổng:", cong(a, b))
    print("Hiệu:", tru(a, b))
    print("Tích:", nhan(a, b))
    print("Thương:", chia(a, b))
a()
    
    
def luy_thua(x, k):
    kq = 1
    for i in range(k):
        kq *= x
    return kq

def b():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    n = int(input("Nhập n: "))
    mu = b + n
    print("Đáp án 1 =", luy_thua(a, mu))
b()
    
def c():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    n = int(input("Nhập n: "))
    mu = n + 2
    kq = luy_thua(b, mu) * a
    print("Đáp án 2 =", kq)
c()