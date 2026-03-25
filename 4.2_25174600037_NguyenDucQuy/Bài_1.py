import math
n = int(input("Nhập n: "))

s1 = sum(i**2 for i in range(1, n + 1))
s2 = sum((2*i + 1)**3 for i in range(n + 1))
s3 = sum((2*i)**4 for i in range(1, n + 1))
s4 = sum(((-1)**(i-1)) / i for i in range(1, n + 1))
s5 = sum(1 / (i * (i + 1)) for i in range(1, n + 1))
s6 = sum(1 / math.sqrt(i) for i in range(2, n + 1))
print(f"Kết quả: S1={s1}, S2={s2}, S3={s3}, S4={s4:.4f}, S5={s5:.4f}, S6={s6:.4f}")
#
import math
n = int(input("Nhập n: "))
s1 = s2 = s3 = s4 = s5 = s6 = 0
i = 1

while i <= n:
    s1 += i**2
    s2 += (2*(i-1) + 1)**3 
    s3 += (2*i)**4
    s4 += ((-1)**(i-1)) / i
    s5 += 1 / (i * (i + 1))
    if i >= 2:
        s6 += 1 / math.sqrt(i)
    i += 1
s2 += (2*n + 1)**3

print(f"Kết quả: S1={s1}, S2={s2}, S3={s3}, S4={s4:.4f}, S5={s5:.4f}, S6={s6:.4f}")
