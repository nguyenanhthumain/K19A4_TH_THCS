# a:
m = int(input())
n = int(input())

A = []

for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)
# b:
tong = 0
for row in A:
    for x in row:
        tong += x

print("Tổng =", tong)