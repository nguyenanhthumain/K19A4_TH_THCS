n = 1
while n <= 1000:
    if n >= 2:
        ket_qua = True
        i = 2
        while i * i <= n:
            if n % i == 0:
                ket_qua = False
                break
            i = i + 1
        if ket_qua:
            print(n, end=" ")   
    n = n + 1