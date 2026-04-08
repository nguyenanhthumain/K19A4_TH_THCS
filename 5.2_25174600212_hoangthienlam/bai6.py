import random
A = [random.randint(1, 99999) for _ in range(1000)]
# Cách 1:
A_sorted = sorted(A)
# Cách 2
A_manual = A[:] # Copy list
n = len(A_manual)
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if A_manual[j] < A_manual[min_idx]:
            min_idx = j
    A_manual[i], A_manual[min_idx] = A_manual[min_idx], A_manual[i]
print("Cách 1 (5 số đầu):", A_sorted[:5])
print("Cách 2 (5 số đầu):", A_manual[:5])