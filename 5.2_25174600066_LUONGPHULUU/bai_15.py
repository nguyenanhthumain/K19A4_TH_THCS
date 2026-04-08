X, Y = map(int, input().split())

matrix = [[i * j for j in range(Y)] for i in range(X)]

for row in matrix:
    print(row)