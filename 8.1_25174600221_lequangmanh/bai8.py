def bai8():
    print("=== TINH HINH HOC ===")

    # Hình tròn
    r = float(input("Nhap ban kinh r: "))
    if r > 0:
        cv = 2 * 3.14 * r
        dt = 3.14 * r * r
        print("Hinh tron - CV:", cv, "DT:", dt)
    else:
        print("Ban kinh khong hop le")

    # Hình vuông
    a = float(input("Nhap canh a: "))
    if a > 0:
        cv = 4 * a
        dt = a * a
        print("Hinh vuong - CV:", cv, "DT:", dt)
    else:
        print("Canh khong hop le")

    # Hình chữ nhật
    dai = float(input("Nhap chieu dai: "))
    rong = float(input("Nhap chieu rong: "))
    if dai > 0 and rong > 0:
        cv = 2 * (dai + rong)
        dt = dai * rong
        print("HCN - CV:", cv, "DT:", dt)
    else:
        print("Kich thuoc khong hop le")

    # Hình tam giác (3 cạnh)
    a = float(input("Canh a: "))
    b = float(input("Canh b: "))
    c = float(input("Canh c: "))

    if a + b > c and a + c > b and b + c > a:
        cv = a + b + c
        p = cv / 2
        dt = (p * (p-a) * (p-b) * (p-c)) ** 0.5
        print("Tam giac - CV:", cv, "DT:", dt)
    else:
        print("Khong phai tam giac")
        

bai8()