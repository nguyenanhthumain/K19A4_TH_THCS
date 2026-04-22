# a:
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def tim_ucln():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    print("UCLN =", ucln(a, b))
# b:
def bcnn(a, b):
    return a * b // ucln(a, b)
def tim_bcnn():
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    print("BCNN =", bcnn(a, b))
# c:
def rut_gon():
    tu = int(input("Nhập tử: "))
    mau = int(input("Nhập mẫu: "))
    u = ucln(tu, mau)
    print("Phân số rút gọn:", tu//u, "/", mau//u)
# d:
def tim_min_max():
    n = int(input("Nhập số lượng phần tử: "))
    x = int(input("Nhập số thứ 1: "))
    min_val = max_val = x
    for i in range(2, n+1):
        x = int(input(f"Nhập số thứ {i}: "))
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    print("Nhỏ nhất:", min_val)
    print("Lớn nhất:", max_val)
# ====Gọi chương trình====
print("Câu a:")
tim_ucln()
print("Câu b:")
tim_bcnn()
print("Câu c:")
rut_gon()
print("Câu d:")
tim_min_max()