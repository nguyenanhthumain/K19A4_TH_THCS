def luy_thua(n):
    x = int(input("Nhập x: "))
    kq = 1
    for i in range(n):
        kq *= x
    return kq

n = int(input("Nhập n: "))
print(luy_thua(n))