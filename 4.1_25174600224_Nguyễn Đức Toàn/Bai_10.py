n = int(input("Nhập n: "))
for x in range(2, n+1):
    so_nguyen_to = True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            so_nguyen_to = False
            break
    if so_nguyen_to:
        print(x)
        
        
        


n = int(input("Nhập n: "))
for x in range(1, n+1):
    tong = 0
    for i in range(1, x):
        if x % i == 0:
            tong += i
    if tong == x:
        print(x)