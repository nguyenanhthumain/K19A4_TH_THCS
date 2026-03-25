# Cách 1 while:
while True:
    n = int(input("Nhập n > 0: "))
    if n > 0:
        break
    print("Nhập lại!")
i = 1
S1 = S2 = S3 = S4 = S5 = 0
S6 = 0
while i <= n:
    S1 += i**2
    S2 += (2*i - 1)**3
    S3 += (2*i)**4
    S4 += ((-1)**(i-1)) / i
    S5 += 1 / (i * (i * 1))
    if i >= 2:
        S6 += 1 / math.sqrt(i)
    i += 1
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)
print("S5 =", S5)
print("S6 =", S6)
# Cách 2 for:
while True:
    n = int(input("Nhập n > 0: "))
    if n > 0:
        break
    print("Nhập lại!")
import math
# a. S1
S1 = 0
for i in range(1, n + 1):
    S1 += i**2
# b. S2
S2 = 0
for i in range(0, n + 1):
    S2 += (2*i + 1)**3
# c. S3
S3 = 0
for i in range(1, n + 1):
    S3 += (2*i)**4
# d. S4
S4 = 0
for i in range(1, n + 1):
    S4 += ((-1)**(i-1)) / i
# e. S5
S5 = 0
for i in range(1, n + 1):
    S5 += 1 / (i* (i + 1))
# f. S6
S6 = 0
for i in range(2, n + 1):
    S6 += 1 / math.sqrt(i)
print("S1 =", S1)
print("S2 =", S2)
print("S3 =", S3)
print("S4 =", S4)
print("S5 =", S5)
print("S6 =", S6)