# câu a
def la_so_nguyen_to(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Nhập n: "))

if la_so_nguyen_to(n):
    print(n, "là số nguyên tố")
else:
    print(n, "không phải số nguyên tố")

# câu b
def la_so_hoan_hao(n):
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong = tong + i

    if tong == n:
        return True
    else:
        return False

n = int(input("Nhập n: "))

if la_so_hoan_hao(n):
    print(n, "là số hoàn hảo")
else:
    print(n, "không phải số hoàn hảo")

# câu c
def la_doi_xung(n):
    s = str(n)
    return s == s[::-1]

dem = 0

print("Các số đối xứng <= 1000:")

for i in range(0, 1000):
    if la_doi_xung(i):
        print(f"{i:5}", end=" ")
        dem = dem + 1

        if dem % 15 == 0:
            print()       