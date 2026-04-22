# Bai 10
def in_cac_uoc_so(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")

print("=== Bai 10 ===")
n = int(input("Nhap n: "))
in_cac_uoc_so(n)