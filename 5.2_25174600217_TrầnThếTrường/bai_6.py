A = [(i * 37 + 12345) % 99999 + 1 for i in range(1000)]

print("10 phần tử đầu của A:", A[:10])

A_sorted = sorted(A)
print("Tăng dần (sorted):", A_sorted[:10])

A_sorted_desc = sorted(A, reverse=True)
print("Giảm dần (sorted):", A_sorted_desc[:10])

A2 = A.copy()
n = len(A2)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if A2[j] > A2[j + 1]:
            A2[j], A2[j + 1] = A2[j + 1], A2[j]

print("Tăng dần (không dùng sorted):", A2[:10])

A3 = A.copy()

for i in range(n - 1):
    for j in range(n - 1 - i):
        if A3[j] < A3[j + 1]:
            A3[j], A3[j + 1] = A3[j + 1], A3[j]

print("Giảm dần (không dùng sorted):", A3[:10])