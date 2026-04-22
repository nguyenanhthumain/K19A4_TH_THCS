def in_ma_ascii():
    while True:
        ky_tu = input("Nhập ký tự (ESC để thoát): ")
        if ky_tu and ord(ky_tu[0]) == 27:
            print("Kết thúc chương trình.")
            break
        if ky_tu:
            print("ASCII:", ord(ky_tu[0]))
in_ma_ascii()