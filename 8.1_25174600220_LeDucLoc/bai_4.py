#a
def tinh_S(n):
    ket_qua = 1
    for i in range(n + 1):
        ket_qua = ket_qua * (2 * i + 1)
    return ket_qua
n = int(input("Nhập số nguyên n: "))
print("Kết quả P là: ", tinh_S(n))

#b
def tinh_S(n):
    tong = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            tong += i
        else:
            tong -= i
    return tong
n = int(input("Nhập số nguyên n: "))
print(f"Kết quả S({n}) là: {tinh_S(n)}")

#c
def tinh_S(n):
    n = int(input("Nhập số nguyên n: "))
    tong_lon = 0
    tong_con = 0
    for i in range(1, n + 1):
        tong_con += i
        tong_lon += tong_con
    return tong_lon
n = int(input("Nhập số nguyên n: "))
print(f"Kết quả S({n}) là: {tinh_S(n)}")

#d
def tinh_S(x, y, n_d):
    x = float(input("Nhập x: "))
    y = float(input("Nhập y: "))
    luy_thua_xy = x ** y
    tong_sigma = 0
    for k in range(1, n_d + 1):
        tong_sigma += (x + 32 * y + y ** k)
    return luy_thua_xy + tong_sigma

while True:
    n_d = int(input("Nhập n (điều kiện n > 1): "))
    if n_d > 1:
        break
        print(f"Kết quả P(x, y) là: {tinh_S(x, y, n_d)}")
    else:
        print("=> Lỗi: n phải lớn hơn 1. Vui lòng nhập lại!")    