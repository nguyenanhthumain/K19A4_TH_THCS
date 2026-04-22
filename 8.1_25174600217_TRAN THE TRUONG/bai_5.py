def in_ma_ASCII():
    while True:
        ch = input("Nhập một ký tự (gõ ESC để thoát): ")

        if ch == "ESC":
            print("Kết thúc chương trình.")
            break

        if len(ch) != 1:
            print("Vui lòng chỉ nhập 1 ký tự!")
            continue

        print("Mã ASCII của", ch, "là:", ord(ch))

in_ma_ASCII()