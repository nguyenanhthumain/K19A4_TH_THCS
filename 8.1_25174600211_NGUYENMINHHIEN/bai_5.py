def ascii_ky_tu():
    while True:
        ch = input("Nhap ky tu (ESC de dung): ")
        if ch == "ESC":
            break
        print("ASCII:", ord(ch))
ascii_ky_tu()