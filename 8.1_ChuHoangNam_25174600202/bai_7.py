#cau7
def tim_ucln(a, b):
    while b != 0:
        du = a % b
        a = b
        b = du
    return a

def tim_bcnn(a, b):
    ucln = tim_ucln(a, b)
    return (a * b) // ucln

# a b
so1 = int(input("Nhap so a: "))
so2 = int(input("Nhap so b: "))
print("UCLN cua 2 so la:", tim_ucln(so1, so2))
print("BCNN cua 2 so la:", tim_bcnn(so1, so2))

#c
tu = int(input("Nhap tu so: "))
mau = int(input("Nhap mau so: "))
ucln_ps = tim_ucln(tu, mau)
print(f"Phan so rut gon la: {tu // ucln_ps}/{mau // ucln_ps}")

#d
n = int(input("Nhap so luong n: "))
so_dau = int(input("Nhap so thu 1: "))
min_val = so_dau
max_val = so_dau
for i in range(2, n + 1):
    so = int(input(f"Nhap so thu {i}: "))
    if so < min_val: min_val = so
    if so > max_val: max_val = so
print("So nho nhat la:", min_val)
print("So lon nhat la:", max_val)