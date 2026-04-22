import random

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def tao_list_va_in_snt():
    n = int(input("Nhập n: "))
    lst = []

    for i in range(n):
        lst.append(random.randint(1, 100))

    print("List:", lst)

    print("Số nguyên tố:")
    for x in lst:
        if la_so_nguyen_to(x):
            print(x, end=" ")

tao_list_va_in_snt()