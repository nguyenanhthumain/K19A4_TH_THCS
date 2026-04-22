def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def a():
    n = int(input("Nhập số nguyên dương n: "))
    if la_so_nguyen_to(n):
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải số nguyên tố")
a()



def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
def b():
    n = int(input("Nhập số nguyên dương n: "))
    if la_so_hoan_hao(n):
        print(n, "là số hoàn hảo")
    else:
        print(n, "không phải số hoàn hảo")
b()



def la_so_doi_xung(n):
    s = str(n)
    return s == s[::-1]
def c():
    so = 0
    for i in range(1, 1000):
        if la_so_doi_xung(i):
            print(f"{i:5}", end=" ")
            so += 1
            if so % 15 == 0:
                print()
c()