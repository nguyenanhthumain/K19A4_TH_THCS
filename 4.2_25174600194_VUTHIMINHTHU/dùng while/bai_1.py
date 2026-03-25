n = int(input("Nhập n (số nguyên dương): "))
while True:
    if n>0:
        break
S1=S2=S3=S4=S5=S6=0
for i in range(1,n+1):
        S1 += i**2
print(f"Tổng S1:",S1)
for i in range (0,n+1):
        S2 +=(2*i +1)**3
print(f"Tổng S2:",S2)
for i in range(1,n+1):
        S3 +=(2*i)**4
print(f"Tổng S3:",S3)
for i in range(1,n+1):
        S4 +=((-1)**(i-1)/i)
print(f"Tổng S4:",S4)
for i in range (1,n+1):
        S5 += 1/(i*(i+1))
print(f"Tổng S5:",S5)
for i in range(2,n+1):
        S6 += 1/(i**(1/2))
print(f"Tổng S6",S6)
