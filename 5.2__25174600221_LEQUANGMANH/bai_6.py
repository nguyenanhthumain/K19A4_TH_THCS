import random
A = [random.randint(1, 99999) for _ in range(1000)]

# Cách 1: Dùng sorted()
cach1 = sorted(A)

# Cách 2: Không dùng sorted (Bubble Sort)
cach2 = A[:]
n = len(cach2)
for i in range(n):
    for j in range(0, n-i-1):
        if cach2[j] > cach2[j+1]:
            cach2[j], cach2[j+1] = cach2[j+1], cach2[j]

print("6. Đã sắp xếp xong bằng 2 cách.")