def tinh_luy_thua():
    a = int(input("Nhap so tu nhien a: "))
    n = int(input("Nhap so mu n: "))
    kq = 1
    for i in range(n):
        kq = kq * a
    print("Ket qua:", kq)
tinh_luy_thua()
    