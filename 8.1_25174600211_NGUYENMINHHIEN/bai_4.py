def tong_1(n):
    s = 0
    for i in range(n+1):
        s += i
    return s
def tong_2(n):
    s = 0
    for i in range(n+1):
        s += i*i
    return s
def giai_thua(n):
    gt = 1
    for i in range(1, n+1):
        gt *= i
    return gt
def tong_giai_thua(n):
    s = 0
    for i in range(1, n+1):
        s += giai_thua(i)
    return s
n = int(input("Nhap n: "))
print(tong_1(n))
print(tong_2(n))
print(giai_thua(n))
print(tong_giai_thua(n))