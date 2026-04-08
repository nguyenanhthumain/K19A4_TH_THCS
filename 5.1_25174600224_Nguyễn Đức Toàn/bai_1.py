n = int(input("Nhập n: "))
m = int(input("Nhập m: "))

list = [0] * n

for i in range(n):
    list[i] = (i + 1) ** 2

if m >= n:
    print(list)
else:
    print(list[:m])