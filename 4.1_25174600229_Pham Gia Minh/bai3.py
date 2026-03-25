a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

res = 0
while b > 0:
    if b % 2 != 0:
        res += a
    a = a + a
    b = b // 2

print(f"Ket qua = {res}")