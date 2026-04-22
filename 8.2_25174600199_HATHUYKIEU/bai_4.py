def dao_nguoc_danh_sach(ds):
    return ds[::-1]
n = int(input("Nhập số phần tử: "))
ds = []
for i in range(n):
    x = int(input("Nhập phần tử: "))
    ds.append(x)
print("Danh sách ban đầu:", ds)
print("Danh sách sau khi đảo ngược:", dao_nguoc_danh_sach(ds))