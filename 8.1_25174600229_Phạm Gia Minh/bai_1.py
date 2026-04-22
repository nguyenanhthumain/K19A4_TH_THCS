def luy_thua(a, n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua = ket_qua * a
    return ket_qua

a = int(input("Nhập số a: "))
n = int(input("Nhập số n: "))

kq = luy_thua(a, n)
print("Kết quả a^n =", kq)