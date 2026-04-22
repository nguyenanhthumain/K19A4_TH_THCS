def in_ascii():
    while True:
        c = input("Nhập ký tự (ESC để thoát): ")
        if c == chr(27):
            break
        print(ord(c))

in_ascii()
