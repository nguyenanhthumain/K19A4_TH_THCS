# a:
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def kiem_tra_nguyen_to():
    n = int(input("Nhập số nguyên dương n: "))
    if la_so_nguyen_to(n):
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")

# b:
def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
def kiem_tra_hoan_hao():
    n = int(input("Nhập số nguyên dương n: "))
    if la_so_hoan_hao(n):
        print(n, "là số hoàn hảo")
    else:
        print(n, "không phải là số hoàn hảo")

# c:
def la_so_doi_xung(n):
    temp = n
    dao = 0
    while temp > 0:
        dao = dao * 10 + temp % 10
        temp //= 10
    return dao == n
def in_so_doi_xung():
    dem = 0
    print("Các số đối xứng <= 1000:")
    for i in range(1, 1001):
        if la_so_doi_xung(i):
            print(f"{i:5}", end="")
            dem += 1
            if dem % 15 == 0:
                print()
# ====== GỌI CHƯƠNG TRÌNH ======
print("Câu a:")
kiem_tra_nguyen_to()
print("\n Câu b:")
kiem_tra_hoan_hao()
print("\n Câu c:")
in_so_doi_xung()