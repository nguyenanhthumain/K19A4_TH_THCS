#bai5
def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def la_so_hoan_hao(x):
    if x < 2:
        return False
    tong = 0
    for i in range(1, x):
        if x % i == 0:
            tong += i
    return tong == x
n = int(input("nhap n: "))
while n < 1:
    print("n phai lon hon 0, nhap lai")
    n = int(input("nhap n: "))
danhsach = list(range(1, n+1))
nguyen_to = []
hoan_hao = []
for so in danhsach:
    if la_so_nguyen_to(so):
        nguyen_to.append(so)
    if la_so_hoan_hao(so):
        hoan_hao.append(so)
print("danh sach so nguyen to:", nguyen_to)
print("danh sach so hoan hao:", hoan_hao)