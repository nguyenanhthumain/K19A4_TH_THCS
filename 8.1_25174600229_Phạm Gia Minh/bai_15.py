from functools import reduce

def bai_15a():
    # a)
    list_chan = [i for i in range(1, 101) if i % 2 == 0]
    print(list_chan)

def bai_15b():
    # b)
    n = int(input("Nhap n: "))
    ds = list(range(1, n + 1))
    
    ds_chan = list(filter(lambda x: x % 2 == 0, ds))
    
    if len(ds_chan) > 0:
        tong = reduce(lambda x, y: x + y, ds_chan)
    else:
        tong = 0
        
    print(ds_chan)
    print(tong)




