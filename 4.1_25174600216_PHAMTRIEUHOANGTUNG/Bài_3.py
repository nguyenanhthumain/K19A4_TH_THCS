a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
def nhan_an_do(a, b):
    if b == 0:
        return 0
    if b % 2 == 0:
        return nhan_an_do(a, b // 2) + nhan_an_do(a, b // 2)
    else:
        return nhan_an_do(a, b // 2) + nhan_an_do(a, b // 2) + a