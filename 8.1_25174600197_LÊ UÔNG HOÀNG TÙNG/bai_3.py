def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
def la_so_doi_xung(n):
    return str(n) == str(n)[::-1]
def bai_3():
    n = int(input("nhap so nguyen duong n: "))
    #a)
    if la_so_nguyen_to(n):
        print(n, "la so nguyen to")
    else:
        print(n, "khong phai so nguyen to")
    #b)
    if la_so_hoan_hao(n):
        print(n, "la so hoan hao")
    else:
        print(n, "khong phai so hoan hao")
    #c)
    print("cac so doi xung <= 1000:")
    dem = 0
    for i in range(0, 1001):
        if la_so_doi_xung(i):
            print(f"{i:5}", end="")
            dem += 1
            if dem % 15 == 0:
                print()
bai_3()