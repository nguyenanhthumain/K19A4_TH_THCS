n = int(input("Nhap n: "))
dem = 0

for i in range(1, n + 1):
    if n % i == 0:
        dem = dem + 1

if dem == 2:
    print(f"{n} la so nguyen to")
else:
    print(f"{n} khong phai la so nguyen to")
