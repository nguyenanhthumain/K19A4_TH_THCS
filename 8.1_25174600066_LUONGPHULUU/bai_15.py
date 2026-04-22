from functools import reduce
def chuong_trinh():
# a:
    ds_100 = list(range(1, 101))
    chan_100 = list(filter(lambda x: x % 2 == 0, ds_100))
    print("Số chẵn từ 1 đến 100:")
    print(chan_100)
    
# b:
    n = int(input("\nNhập n: "))
    ds = list(map(int, input("Nhập các số: ").split()))
    chan = list(filter(lambda x: x % 2 == 0, ds))
    tong = reduce(lambda a, b: a + b, chan, 0)
    
    print("Danh sách:", ds)
    print("Số chẵn:", chan)
    print("Tổng số chẵn:", tong)

chuong_trinh()