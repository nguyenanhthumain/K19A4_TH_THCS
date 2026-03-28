"""Viết chương trình nhập vào từ bàn phím tử số và mẫu số của một phân số, nếu
mẫu số là 0 thì nhập lại."""

n = 0
while n <= 0:
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        print("Vui lòng nhập lại!")
#FOR
s1 = 0
for i in range(1, n + 1):
    s1 += i**2
print(f"S1 = {s1}")

s2 = 0
for i in range(n + 1):
    s2 += (2*i + 1)**3
print(f"S2 = {s2}")

s3 = 0
for i in range(1, n + 1):
    s3 += (2*i)**4
print(f"S3 = {s3}")

s4 = 0
for i in range(1, n + 1):
    s4 += ((-1)**(i-1))/i
print(f"S4 = {s4}")

s5 = 0
for i in range(1, n + 1):
    s5 += 1/(i*(i+1))
print(f"S5 = {s5}")

s6 = 0
for i in range(2, n + 1):
    s6 += 1 / (i**0.5)
print(f"S6 = {s6}")






#WHILE
s1 = 0
i = 1
while i <= n: 
    s1 += i**2
    i += 1
print(f"S1 = {s1}")

s2 = 0
i = 0
while i <= n:
    s2 += (2*i + 1)**3
    i += 1
print(f"S2 = {s2}")

s3 = 0
i = 1
while i <= n: 
    s3 += (2*i)**4
    i += 1
print(f"S3 = {s3}")

s4 = 0
i = 1
while i <= n: 
    s4 += ((-1)**(i-1)) / i
    i += 1
print(f"S4 = {s4}")

s5 = 0
i = 1
while i <= n: 
    s5 += 1 / (i * (i + 1))
    i += 1
print(f"S5 = {s5}")

s6 = 0
i = 2
while i <= n: 
    s6 += 1 / (i**0.5)
    i += 1
print(f"S6 = {s6}")