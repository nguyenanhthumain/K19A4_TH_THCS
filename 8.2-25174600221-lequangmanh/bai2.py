import random

def tao_list_va_binh_phuong():
    n = int(input("Nhập n: "))
    lst = []

    for i in range(n):
        lst.append(random.randint(1, 100))

    print("List:", lst)

    binh_phuong = list(map(lambda x: x*x, lst))
    print("Bình phương:", binh_phuong)

tao_list_va_binh_phuong()