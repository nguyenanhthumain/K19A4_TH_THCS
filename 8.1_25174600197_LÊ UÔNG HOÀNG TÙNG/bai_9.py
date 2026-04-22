def tinh_toan(a, b):
    print("cong =", a+b)
    print("tru =", a-b)
    print("nhan =", a*b)
    if b != 0:
        print("chia =", a/b)
    else:
        print("khong chia duoc")
def luy_thua(a, b, n):
    print("a^(b+n) =", a**(b+n))
    print("b^(n+2)*a =", (b**(n+2))*a)
def bai_9():
    a = int(input("nhap a: "))
    b = int(input("nhap b: "))
    tinh_toan(a,b)
    n = int(input("nhap n: "))
    luy_thua(a,b,n)
bai_9()