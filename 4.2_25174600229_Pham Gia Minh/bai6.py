while True:
    s = input("Nhap so > 100: ")
    if int(s) > 100: break

# FOR
print("For:", sum(int(c) for c in s))

# WHILE
n = int(s); t = 0
while n > 0:
    t += n % 10
    n //= 10
print("While:", t)