n = int(input("Nhập số nguyên dương n: "))
print(f"Các số từ {n} đến {n**2}:")
for i in range(n, n**2 + 1):
    print(i, end=" ")
print()