#bài 4
def dao_nguoc(ds):
    kq = []
    for i in range(len(ds)-1, -1, -1):
        kq.append(ds[i])
    return kq

s = input()
ds = list(map(int, s.split()))
print(dao_nguoc(ds))