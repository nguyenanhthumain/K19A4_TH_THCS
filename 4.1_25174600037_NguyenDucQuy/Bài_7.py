while True:
    print("\n1.Cộng  2.Trừ  3.Nhân  4.Chia  0.Thoát")
    chon = int(input("Chọn: "))

    if chon == 0:
        break

    n = float(input("Nhập n: "))
    m = float(input("Nhập m: "))

    if chon == 1:
        print("KQ:", n + m)
    elif chon == 2:
        print("KQ:", n - m)
    elif chon == 3:
        print("KQ:", n * m)
    elif chon == 4:
        if m != 0:
            print("KQ:", n / m)
        else:
            print("Không chia được")