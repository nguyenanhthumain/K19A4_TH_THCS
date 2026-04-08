n = int(input("Nhập n: "))

t = tuple(int(input()) for _ in range(n))

odd = tuple(x for x in t if x % 2 != 0)

print(odd)