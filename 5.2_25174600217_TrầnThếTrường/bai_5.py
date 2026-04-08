A = []
i = 1

while len(A) < 1000:
    x = (i * 37 + 12345) % 99999 + 1
    if x % 7 != 0:
        A.append(x)
    i += 1

print(A)