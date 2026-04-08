tup = tuple(map(int, input("Nhập tuple: ").split()))
n = int(input("Nhập n: "))

odd = []

for x in tup:
    if x % 2 != 0:
        odd.append(x)

result = tuple(odd[:n])

print(result)