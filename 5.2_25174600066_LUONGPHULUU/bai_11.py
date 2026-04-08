import random
n = int(input("Nhập n: "))

# Nhập danh sách A
A = [int(input()) for _ in range(n)]
# a:
B = [x for x in A if x % 3 == 0 and x % 5 != 0]
print("B =", B)
# b:
C = [x**2 for x in A]
print("C =", C)
# c:
D = [random.choice([x for x in A if x % 3 == 0]) for _ in range(len(A)) if any(x % 3 == 0 for x in A)]
print("D =", D)