A = []
x = 7
while len(A) < 1000:
    x = (x * 3 + 11) % 100000
    num = x % 99999 + 1
    A.append(num)
print("10 phần tử đầu của A:", A[:10])
# Cách 1:
A_tang1 = sorted(A)
print("Tăng dần (dùng sorted):", A_tang1[:10])
# Cách 2:
A_tang2 = A[:]
n = len(A_tang2)
for i in range(n):
    for j in range(n - i - 1):
        if A_tang2[j] > A_tang2[j + 1]:
            temp = A_tang2[j]
            A_tang2[j] = A_tang2[j + 1]
            A_tang2[j + 1] = temp
print("Tăng dần (không dùng sorted):", A_tang2[:10])