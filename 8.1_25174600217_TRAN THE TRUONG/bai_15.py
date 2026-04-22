#a.
def tao_list_chan_1_100():
    lst = []
    for i in range(1, 101):
        if i % 2 == 0:
            lst.append(i)
    return lst

#b.
def my_reduce(func, lst, init):
    kq = init
    for x in lst:
        kq = func(kq, x)
    return kq

def tong_chan(lst):
    ds_chan = list(filter(lambda x: x % 2 == 0, lst))
    tong = my_reduce(lambda a, b: a + b, ds_chan, 0)
    return tong

def main():
    print("=== Phần a: List số chẵn từ 1 đến 100 ===")
    lst_chan = tao_list_chan_1_100()
    print(lst_chan)

    print("\n=== Phần b: Tính tổng số chẵn trong list 1..n ===")
    n = int(input("Nhập n: "))
    lst = list(range(1, n + 1))
    print("Danh sách:", lst)

    print("Tổng các số chẵn =", tong_chan(lst))

main()