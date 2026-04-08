while True:
    m = int(input("Nhập m: "))
    n = int(input("Nhập n: "))
    if 0 < m < n:
        break
    else:
        print("Sai điều kiện, nhập lại!")
ds = []
for i in range(m, n + 1):
    ds.append(i)
ds_chan = list(filter(lambda x: x % 2 == 0, ds))
print("Danh sách:", ds)
print("Số chẵn:", ds_chan)
