def in_fibonacci(n):
    fib1 = 0
    fib2 = 1
    i =0
    while i<n:
        print(fib1,end = " ")
        fib1,fib2 = fib2,fib1 + fib2
        i += 1
print(f"Dãy fibonacci là:")
in_fibonacci(20)