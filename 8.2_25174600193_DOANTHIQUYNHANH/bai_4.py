def dao_nguoc_danh_sach(ds):
    ket_qua = []
    for i in range(len(ds)-1, -1, -1):
        ket_qua.append(ds[i])
    return ket_qua

ds = list(map(int, input("Nhập các phần tử: ").split()))
print("Danh sách đảo ngược:", dao_nguoc_danh_sach(ds))