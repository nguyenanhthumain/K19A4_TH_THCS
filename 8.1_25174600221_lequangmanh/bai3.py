def kiem_tra_snt(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def kiem_tra_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0: tong += i
    return tong == n

def in_so_doi_xung_1000():
    count = 0
    for n in range(1001):
        s = str(n)
        if s == s[::-1]:
            print(f"{n:0>5}", end=" ")
            count += 1
            if count % 15 == 0: