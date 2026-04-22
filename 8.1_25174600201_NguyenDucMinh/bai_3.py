#câu a
import math

def nhap_n():
    return int(input("Nhập n: "))

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = nhap_n()
if la_so_nguyen_to(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")

#câu b
def nhap_n():
    return int(input("Nhập n: "))

def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            tong += i
    return tong == n


n = nhap_n()
if la_so_hoan_hao(n):
    print(n, "là số hoàn hảo")
else:
    print(n, "không phải số hoàn hảo")

#câu c
def la_so_doi_xung(n):
    return str(n) == str(n)[::-1]


def in_so_doi_xung():
    dem = 0

    for i in range(1, 1001):
        if la_so_doi_xung(i):
            print(f"{i:5}", end="")  # mỗi số 5 ký tự
            dem += 1

            if dem % 15 == 0:  # xuống dòng sau 15 số
                print()


in_so_doi_xung()
