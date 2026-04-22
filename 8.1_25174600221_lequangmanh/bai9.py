def bai9():
    print("=== TINH TOAN ===")

    # nhập a
    while True:
        try:
            a = int(input("Nhap a: "))
            break
        except:
            print("Nhap so nguyen!")

    # nhập b
    while True:
        try:
            b = int(input("Nhap b: "))
            break
        except:
            print("Nhap so nguyen!")

    # nhập n
    while True:
        try:
            n = int(input("Nhap n: "))
            break
        except:
            print("Nhap so nguyen!")

    # phép toán cơ bản
    print("Cong:", a + b)
    print("Tru:", a - b)
    print("Nhan:", a * b)

    if b != 0:
        print("Chia:", a / b)
    else:
        print("Khong the chia cho 0")

    # lũy thừa
    print("a^(b+n):", a ** (b + n))
    print("b^(n+2a):", b ** (n + 2*a))


bai9()