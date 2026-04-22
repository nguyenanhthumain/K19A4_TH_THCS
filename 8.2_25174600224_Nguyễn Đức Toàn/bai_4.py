def dao_nguoc_danh_sach(ds):
    kq = []
    for i in range(len(ds) - 1, -1, -1):
        kq.append(ds[i])
    return kq
ds = list(map(int, input("Nhập danh sách: ").split()))
print("Danh sách đảo ngược:", dao_nguoc_danh_sach(ds))