n = int(input("Nhập m: "))
m = int(input("Nhập n: "))
lst = []
for i in range(1, n + 1):
    lst.append(i * i)

if m >= n:
    print(lst)
else:
    print(lst[:m])