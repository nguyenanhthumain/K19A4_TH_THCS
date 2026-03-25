import math
while True:
    n = int(input("Nhap n: "))
    if n > 0: break

# FOR
s1 = sum(i**2 for i in range(1, n + 1))
s2 = sum(i**3 for i in range(1, 2*n + 2, 2))
s3 = sum(i**4 for i in range(2, 2*n + 1, 2))
s4 = sum(((-1)**(i-1)) / i for i in range(1, n + 1))
s5 = sum(1 / (i * (i + 1)) for i in range(1, n + 1))
s6 = sum(1 / math.sqrt(i) for i in range(2, n + 1))
print(f"For: {s1}, {s2}, {s3}, {s4}, {s5}, {s6}")

# WHILE
i = 1; w1=w2=w3=w4=w5=w6 = 0
while i <= n:
    w1 += i**2
    w2 += (2*i-1)**3
    w3 += (2*i)**4
    w4 += ((-1)**(i-1)) / i
    w5 += 1 / (i * (i + 1))
    if i >= 2: w6 += 1 / math.sqrt(i)
    i += 1
w2 += (2*n+1)**3
print(f"While: {w1}, {w2}, {w3}, {w4}, {w5}, {w6}")