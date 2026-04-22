import random

n = int(input("Nhập n: "))
ds = []

for i in range(n):
    ds.append(random.randint(1, 10))

print("Danh sách ban đầu:", ds)

binh_phuong = list(map(lambda x: x * x, ds))
print("Danh sách bình phương:", binh_phuong)