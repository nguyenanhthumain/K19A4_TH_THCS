import random

def tao_list_va_chan():
    n = int(input("Nhập n: "))
    lst = []

    for i in range(n):
        lst.append(random.randint(1, 100))

    print("List:", lst)

    check_chan = list(map(lambda x: x % 2 == 0, lst))
    print("True nếu chẵn:", check_chan)

tao_list_va_chan()