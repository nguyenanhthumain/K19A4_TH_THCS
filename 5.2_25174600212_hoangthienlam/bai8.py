n = int(input("Nhập n: "))
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(n-1)]
result = ", ".join([str(x) for x in fib[:n+1]])
print(result)