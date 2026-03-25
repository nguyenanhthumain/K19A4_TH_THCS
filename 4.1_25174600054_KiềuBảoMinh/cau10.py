n = int(input("Nhập n: "))
x = 1
while x <= n:
    if x >= 2:
        ket_qua = True
        i = 2
        while i < x:
            if x % i == 0:
                ket_qua = False
                break
            i = i + 1
        if ket_qua == True:
            print(x, end=" ")
    x = x + 1

n = int(input("\nNhập n: "))
x = 1
while x <= n:
    tong = 0
    i = 1
    while i < x:
        if x % i == 0:
            tong = tong + i
        i = i + 1
    if tong == x and x != 0:
        print(x, end=" ")
    x = x + 1