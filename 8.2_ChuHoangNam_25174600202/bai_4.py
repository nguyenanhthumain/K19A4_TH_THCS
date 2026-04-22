#cau4
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    val = input("Nhap phan tu thu " + str(i+1) + ": ")
    ds.append(val)

ds_dao = []
for i in range(len(ds) - 1, -1, -1):
    ds_dao.append(ds[i])

print("Danh sach sau khi dao:", ds_dao)