import random

day_A = [random.randint(1, 99999) for _ in range(1000)]
n = len(day_A)
for i in range(n):
    for j in range(0, n - i - 1):
        if day_A[j] > day_A[j + 1]:
            day_A[j], day_A[j + 1] = day_A[j + 1], day_A[j]
print("Dãy số sau khi đã sắp xếp tăng dần:")
print(day_A[:20])