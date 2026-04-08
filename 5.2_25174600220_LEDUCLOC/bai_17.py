"""Ma trận mxn (m hàng, n cột) có thể được mô tả bởi danh sách như sau: A =
|[a11, a12, . . . a1n],[a21, a22, . . . , a2n], . . . ,[am1, am2, . . . , amn]]. Thực hiện các
công việc sau:
a. Viết chương trình nhập vào ma trận A với các phần tử aij là các số tự nhiên
được nhập từ bàn phím.
b. Tính tổng các phần tử của Ma trận A."""

# a
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

A = []

for i in range(m):
    hang = []
    for j in range(n):
        gia_tri = int(input(f"Nhập phần tử a[{i+1}][{j+1}]: "))
        hang.append(gia_tri)
    A.append(hang)

print("\nMa trận A đã nhập là:")
for hang in A:
    print(hang)

# b
tong_ma_tran = 0

for hang in A:
    for phan_tu in hang:
        tong_ma_tran += phan_tu
print(f"Tổng tất cả các phần tử của ma trận A là: {tong_ma_tran}")