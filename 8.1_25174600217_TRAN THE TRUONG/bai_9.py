def luy_thua(x, y):
    kq = 1
    for i in range(y):
        kq *= x
    return kq

def tinh_toan(a, b):
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)

    if b == 0:
        print("a / b = Không thể chia cho 0")
    else:
        print("a / b =", a / b)

def tinh_luy_thua_dac_biet():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    n = int(input("Nhập n: "))

    mu1 = b + n
    mu2 = n + 2 * a

    print("a^(b+n) =", luy_thua(a, mu1))
    print("b^(n+2a) =", luy_thua(b, mu2))

def main():
    print("Phép tính số học")
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    tinh_toan(a, b)

    print("\n Tính lũy thừa đặc biêt")
    tinh_luy_thua_dac_biet()

main()