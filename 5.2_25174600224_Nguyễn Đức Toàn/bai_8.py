n=int(input("Nhập n: "))

fib=[0,1]
[fib.append(fib[-1]+fib[-2]) for i in range(n-1)] 

for i in range(len(fib)):
    if i==len(fib)-1:
        print(fib[i])
    else:
        print(fib[i], end=", ")