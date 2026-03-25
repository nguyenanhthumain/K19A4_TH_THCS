n = int(input("Nhap n: "))

print("Cac so nguyen to la:")
for i in range(2, n + 1):
    check = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            check = False
            break
    if check:
        print(i, end=" ")

print("\nCac so hoan hao la:")
for i in range(1, n + 1):
    tong = 0
    for j in range(1, i):
        if i % j == 0:
            tong = tong + j
    if tong == i:
        print(i, end=" ")