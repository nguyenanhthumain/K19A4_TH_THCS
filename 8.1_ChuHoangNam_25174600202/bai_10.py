#cau10
n = int(input("Nhap so nguyen duong n: "))
if n <= 0:
    print("Vui long nhap so > 0")
else:
    print(f"Cac uoc cua {n} la:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")