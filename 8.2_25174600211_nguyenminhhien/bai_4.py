def dao_nguoc(ds):
    return ds[::-1]
n = int(input("Nhap n: "))
ds = []
for i in range(n):
    ds.append(int(input("Nhap so: ")))
print("Dao nguoc:", dao_nguoc(ds))