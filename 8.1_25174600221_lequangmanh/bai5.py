def bai5():
    while True:
        ch = input("Nhap 1 ky tu (nhap 0 de thoat): ")

        if ch == "0":
            break

        if len(ch) != 1:
            print("Chi nhap 1 ky tu!")
            continue

        print("ASCII:", ord(ch))

bai5()