def giai_thua(n):
    kq = 1
    for i in range(1, n+1):
        kq *= i
    return kq

n = int(input("Nhập n: "))
print(giai_thua(n))