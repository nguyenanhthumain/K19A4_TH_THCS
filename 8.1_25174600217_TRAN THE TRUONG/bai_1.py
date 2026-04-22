def tinh_luy_thua():
    x = int(input("Nhập số tự nhiên x: "))
    n = int(input("Nhập số mũ n: "))

    ket_qua = 1
    for i in range(n):
        ket_qua = ket_qua * x

    print(f"{x} ^ {n} = {ket_qua}")
tinh_luy_thua()