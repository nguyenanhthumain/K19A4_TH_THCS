n = int(input("Nhập n: "))
for num in range(2, n + 1):
    la_snt = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            la_snt = False
            break
        i += 1
    if la_snt:
        print(num, end=" ")