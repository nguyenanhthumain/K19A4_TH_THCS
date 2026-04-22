def tinh_tong_P(n):
    kq = 1
    for i in range(1,n+1):
        kq *= 2*i +1
        return kq
def tinh_tong_S(n):
    kq = 0
    for i in range(n+1):
        kq += (-1)**(i+1)*i
        return kq
def tinh_S(n):
    tong_lon = 0
    for i in range(1, n + 1):
        tong_con = 0
        for j in range(1, i + 1):
            tong_con += j
        tong_lon += tong_con
    return tong_lon
def tinh_P(x, y, n):
    tong_xich_ma = 0
    for k in range(1, n + 1):
        tong_xich_ma += (x + 32*y + y**k)
    ket_qua = x**y + tong_xich_ma
    return ket_qua
def nhap_so_nguyen_duong():
    while True:
        n = int(input("Nhập số nguyên dương n: "))
        if n > 0:
            return n
        print(f"{n} không phải số nguyên dương")
n = nhap_so_nguyen_duong()
print(f"a. Tổng P(n) = 1x3x5x ...x(2n + 1) với (n >=0):",tinh_tong_P(n))
print(f"b.Tổng S(n) = 1-2+3-4+5-... +((-1)^(n+1))x n với (n>=0):", tinh_tong_S(n))
print(f"c.Tổng S(n) = 1 + (1 + 2) + (1 + 2 + 3) + . . . + (1 + 2 +3+. . +n)",tinh_S(n))
x = float(input("d.Nhập x : "))
y = float(input("Nhập y: "))
n_d = int(input("Nhập n: "))
if n_d > 1:
    print(f"Kết quả P({x}, {y}) là: {tinh_P(x, y, n_d)}")
else:
    print(f"Yêu cầu nhập lại")

