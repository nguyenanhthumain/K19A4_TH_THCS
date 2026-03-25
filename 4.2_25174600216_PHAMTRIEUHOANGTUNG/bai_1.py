while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n > 0:
        break
    print("n phải lớn hơn 0. Vui lòng nhập lại!")

print("CÁCH 1:FOR")
S1_for = sum(i**2 for i in range(1, n + 1))
S2_for = sum((2*i + 1)**3 for i in range(0, n + 1))
S3_for = sum((2*i)**4 for i in range(1, n + 1))
S4_for = sum(((-1)**(i - 1)) / i for i in range(1, n + 1))
S5_for = sum(1 / (i * (i + 1)) for i in range(1, n + 1))
S6_for = sum(1 / (i**0.5) for i in range(2, n + 1))

print(f"S1 = {S1_for}\nS2 = {S2_for}\nS3 = {S3_for}")
print(f"S4 = {S4_for}\nS5 = {S5_for}\nS6 = {S6_for}")

print("CÁCH 2:WHILE")
S1_w = S2_w = S3_w = S4_w = S5_w = S6_w = 0
i, j, k = 1, 0, 2

while i <= n:
    S1_w += i**2
    S3_w += (2*i)**4
    S4_w += ((-1)**(i - 1)) / i
    S5_w += 1 / (i * (i + 1))
    i += 1
    
while j <= n:
    S2_w += (2*j + 1)**3
    j += 1
    
while k <= n:
    S6_w += 1 / (k**0.5)
    k += 1

print(f"S1 = {S1_w}\nS2 = {S2_w}\nS3 = {S3_w}")
print(f"S4 = {S4_w}\nS5 = {S5_w}\nS6 = {S6_w}")