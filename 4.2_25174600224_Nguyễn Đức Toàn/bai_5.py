def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
bcnn = a * b // ucln(a, b)

print(ucln(a, b))
print(bcnn)






def ucln(a, b):
    for i in range(1000):
        if b == 0:
            break
        a, b = b, a % b
    return a

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

bcnn = a * b // ucln(a, b)
print(ucln(a, b))
print(bcnn)