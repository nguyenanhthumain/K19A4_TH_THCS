def in_ma_ascii_đon_gian():
    while True:
        s = input("Nhập ký tự (hoặc nhập 'esc' để thoát): ")
        if s.lower() == 'esc':
            print("Kết thúc chương trình.")
            break
        if len(s) == 1:
            print(f"Ký tự: {s} -> Mã ASCII: {ord(s)}")
        else:
            print("Vui lòng chỉ nhập 1 ký tự duy nhất.")
in_ma_ascii_đon_gian()
