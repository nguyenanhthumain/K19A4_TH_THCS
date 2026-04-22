def ascii():
    while True:
        ch = input("Nhập ký tự: ")
        if ch == "ESC":
            print("Kết thúc chương trình")
            break
        if len(ch) == 0:
            print("Không có ký tự")
            continue
        ky_tu = ch[0]
        print("ASCII của", ky_tu, "là", ord(ky_tu))
ascii()