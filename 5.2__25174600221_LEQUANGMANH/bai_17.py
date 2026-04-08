m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))

# a. Nhập ma trận A
A = []
for i in range(m):
    row = []
    for j in range(n):
        val = int(input(f"Nhập phần tử A[{i}][{j}]: "))
        row.append(val)
    A.append(row)

# Hiện ma trận đã nhập
print("Ma trận A vừa nhập:")
for row in A:
    print(row)

# b. Tính tổng các phần tử
tong = 0
for row in A:
    for element in row:
        tong += element

print(f"Tổng tất cả các phần tử trong ma trận A là: {tong}")