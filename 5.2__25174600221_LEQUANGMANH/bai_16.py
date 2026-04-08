n = int(input("Nhập bậc của ma trận đơn vị n: "))

# Tạo ma trận n x n toàn số 0
A = [[0 for j in range(n)] for i in range(n)]

# Gán giá trị 1 cho đường chéo chính (nơi mà i == j)
for i in range(n):
    A[i][i] = 1

print(f"Ma trận đơn vị bậc {n}:")
for row in A:
    print(row)