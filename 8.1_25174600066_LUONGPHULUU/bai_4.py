# a:
def tinh_a():
    n = int(input("Nhập n (>= 0): "))
    tich = 1
    for i in range(n + 1):
        tich *= (2*i + 1)
    print("P(n) =", tich)
# b:
def tinh_b():
    n = int(input("Nhập n (> 0): "))
    tong = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            tong -= i
        else:
            tong += i
    print("S(n) =", tong)
# c:
def tinh_c():
    n = int(input("Nhập n (>= 0):" ))
    tong = 0
    for i in range(1, n + 1):
        temp = 0
        for j in range(1, i + 1):
            temp += j
        tong += temp
    print("S(n) =", tong)
# d:
def tinh_d():
    x = int(input("Nhập x: "))
    y = int(input("Nhập y: "))
    n = int(input("Nhập n (>1): "))
    luy_thua = 1
    for i in range(y):
        luy_thua *= x
    tong = 0
    for k in range(1, n):
        y_mu_k = 1
        for i in range(k):
            y_mu_k *= y
        tong += (x + 32*y + y_mu_k)
    print("P(x,y) =", luy_thua + tong)
# ====== GỌI CHƯƠNG TRÌNH ======
print("Câu a:")
tinh_a()

print("\n Câu b:")
tinh_b()

print("\n Câu c:")
tinh_c()

print("\n Câu d:")
tinh_d()