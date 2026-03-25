a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

#CÁCH 1:FOR
if a < b:
    so_nho = a
else:
    so_nho = b

ucln_for = 1
for i in range(so_nho, 0, -1):
    if a % i == 0 and b % i == 0:
        ucln_for = i
        break

bcnn_for = (a * b) // ucln_for
print("Cách 1 (FOR) -> UCLN:", ucln_for, "BCNN:", bcnn_for)


#CÁCH 2:WHILE
so_thu_nhat = a
so_thu_hai = b

while so_thu_hai != 0:
    so_du = so_thu_nhat % so_thu_hai
    so_thu_nhat = so_thu_hai
    so_thu_hai = so_du

ucln_while = so_thu_nhat
bcnn_while = (a * b) // ucln_while
print("Cách 2 (WHILE) -> UCLN:", ucln_while, "BCNN:", bcnn_while)