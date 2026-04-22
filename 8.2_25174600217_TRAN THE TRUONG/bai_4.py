def dao_nguoc_ds(ds):
    return ds[::-1]

ds = input("Nhập danh sách (các số cách nhau bởi dấu cách): ").split()
ds = [int(x) for x in ds]
print("Danh sách đảo ngược:", dao_nguoc_ds(ds))