#WHILE
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
tich = a * b

x, y = a, b
while y != 0:
    x, y = y, x % y
ucln = x

bcnn = tich // ucln
print(f"UCLN: {ucln}, BCNN: {bcnn}")

#FOR
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))  
tich = a * b

ucln = 0
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        ucln = i

bcnn = tich // ucln
print(f"UCLN: {ucln}, BCNN: {bcnn}")