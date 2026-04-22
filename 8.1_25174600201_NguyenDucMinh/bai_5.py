def in_ascii():
    while True:
        ky_tu = input("Nhập ký tự (ESC để thoát): ")

        if ky_tu == "":
            continue

        if ord(ky_tu[0]) == 27:
            print("Kết thúc!")
            break

        print("ASCII:", ord(ky_tu[0]))


in_ascii()