def tinh_luy_thua():
    a = int(input("Nhập a: "))
    n = int(input("Nhập n: "))
    
    ket_qua = 1
    for i in range(n):
        ket_qua *= a
    print(ket_qua)
tinh_luy_thua()