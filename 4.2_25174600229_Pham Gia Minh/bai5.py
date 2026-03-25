a = int(input("Nhap a: ")); b = int(input("Nhap b: "))
tich = a * b

# WHILE
x, y = a, b
while y != 0: x, y = y, x % y
print(f"While: UCLN={x}, BCNN={tich/x}")

# FOR
u = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0: u = i
print(f"For: UCLN={u}, BCNN={tich/u}")