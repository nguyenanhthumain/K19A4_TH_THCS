def tinh(a, b):
    print("Cong:", a+b)
    print("Tru:", a-b)
    print("Nhan:", a*b)
    if b != 0:
        print("Chia:", a/b)
def luy_thua(a, n):
    kq = 1
    for i in range(n):
        kq *= a
    return kq
a = int(input("a: "))
b = int(input("b: "))
tinh(a, b)
n = int(input("Nhap mu: "))
print("Luy thua:", luy_thua(a, n))