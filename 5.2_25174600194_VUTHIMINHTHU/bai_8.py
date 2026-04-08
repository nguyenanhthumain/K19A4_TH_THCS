n = int(input("Nhập n: "))
fibonacci = [0, 1]
for i in range(n - 1):
    fibonacci.append(fibonacci[-1] + fibonacci[-2]) 
print(f"Dãy Fibonacci:",end = ",".join(map(str, fibonacci[:n+1])))
