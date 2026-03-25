n = int(input("Nhập giá trị:"))
print(f"Các số nguyên tố từ 1 đến {n}:")
for n in range (2,n+1):
    is_prime = True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            is_prime= False
            break
    if is_prime:
        print(n,end=" ")
print(f"\nCác số hoàn hảo từ 1 đến {n}:")
for n in range(2,n+1):
    tong_uoc = 0
    for i in range(1, (n// 2) + 1):
        if n % i == 0:
            tong_uoc += i
    if tong_uoc == n:
        print(n, end=" ")
