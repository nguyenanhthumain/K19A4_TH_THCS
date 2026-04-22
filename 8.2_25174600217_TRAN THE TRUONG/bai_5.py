import random
def tao_ds_kiem_tra_chan(n):
    ds = [random.randint(1, 100) for _ in range(n)]
    la_chan = list(map(lambda x: x % 2 == 0, ds))
    return ds, la_chan

n = int(input("Nhập số lượng phần tử: "))
ds, check = tao_ds_kiem_tra_chan(n)
print("Danh sách:", ds)
print("Kiểm tra chẵn (True = chẵn):", check)