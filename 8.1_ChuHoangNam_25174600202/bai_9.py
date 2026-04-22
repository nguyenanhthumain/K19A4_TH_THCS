#cau9
def tinh_luy_thua(co_so, so_mu):
    ket_qua = 1
    for i in range(so_mu):
        ket_qua *= co_so
    return ket_qua

a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
n = int(input("Nhap so n: "))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
if b != 0: print(f"{a} / {b} = {a / b}")

print(f"a^(b+n) = {tinh_luy_thua(a, b + n)}")
print(f"b^(n+2a) = {tinh_luy_thua(b, n + 2 * a)}")