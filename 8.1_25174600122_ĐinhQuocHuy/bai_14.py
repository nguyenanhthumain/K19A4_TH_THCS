n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

kq = list(map(lambda x: x*x, arr))
print(kq)