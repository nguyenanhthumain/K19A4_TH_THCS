n = int(input("Nhập số n: "))
 
la_snt = True
 
if n < 2:
    la_snt = False
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            la_snt = False
            break
        i += 1
 
if la_snt:
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải số nguyên tố.")