a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

ket_qua = 0
while b > 0:
    if b % 2 == 1:
        ket_qua += a
    a = a * 2
    b = b // 2

print(ket_qua)