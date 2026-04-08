#bai8
n = int(input("nhap n: "))
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(2, n)]
print(','.join(map(str, fib[:n])))