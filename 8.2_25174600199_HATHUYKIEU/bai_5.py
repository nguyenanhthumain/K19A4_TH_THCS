import random
n = int(input("Nhập n: "))
ds = []
for i in range(n):
    ds.append(random.randint(1, 20))
print("Danh sách:", ds)
ket_qua = list(map(lambda x: True if x % 2 == 0 else False, ds))
print("Kết quả kiểm tra số chẵn:")
print(ket_qua)