n = int(input("Nhập n: "))
ds = []
for i in range(n):
    x = int(input(f"Nhập phần tử {i+1}: "))
    ds.append(x)
binh_phuong = list(map(lambda x: x*x, ds))
print("Danh sách:", ds)
print("Bình phương:", binh_phuong)