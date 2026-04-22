def nhap_so():
    n = int(input("Nhập n: "))
    return n
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = nhap_so()
print(la_so_nguyen_to(n))
def doi_xung(n):
    return str(n) == str(n)[::-1]

dem = 0
for i in range(1000):
    if doi_xung(i):
        print(f"{i:05}", end=" ")
        dem += 1
        if dem % 15 == 0:
            print()