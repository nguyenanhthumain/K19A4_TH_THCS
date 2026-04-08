m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
lst = []
for i in range(m):
    hang = []
    for j in range(n):
        gia_tri = int(input(f"Nhập phần tử A[{i+1}][{j+1}]: "))
        hang.append(gia_tri)
    lst.append(hang)
print("a.Ma trận A: ")
for row in lst:
    print(row)
tong = 0
for hang in lst:
    for phan_tu in hang:
        tong += phan_tu
print(f"b.Tổng tất cả các phần tử của ma trận A là: {tong}")
