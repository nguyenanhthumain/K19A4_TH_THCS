def tinh_luy_thua():
    a = int(input("nhap so tu nhien a: "))
    n = int(input("nhap so mu n: "))
    ket_qua = 1
    for i in range(n):
        ket_qua *= a
    print(f"ket qua {a}^{n} = {ket_qua}")
tinh_luy_thua()