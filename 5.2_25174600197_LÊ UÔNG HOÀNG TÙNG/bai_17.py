#bai17
m = int(input("nhap so hang m: "))
n = int(input("nhap so cot n: "))
ma_tran = []
tong = 0
print("nhap cac phan tu cua ma tran:")
for i in range(m):
    hang = []
    for j in range(n):
        gia_tri = int(input(f"  a[{i}][{j}] = "))
        hang.append(gia_tri)
        tong += gia_tri
    ma_tran.append(hang)
print("ma tran vua nhap:")
for hang in ma_tran:
    print(hang)
print("tong cac phan tu cua ma tran:", tong)