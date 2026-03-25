a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
tich = a * b
x, y = a, b
while y != 0:
    x, y = y, x % y
ucln = x
print(f"UCLN: {ucln}, BCNN: {abs(tich)//ucln}")
#
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
ucln = 1
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        ucln = i
        break
print(f"UCLN: {ucln}, BCNN: {abs(a*b)//ucln}")