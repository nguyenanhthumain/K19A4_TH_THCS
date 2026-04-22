import msvcrt

def in_ma_ascii():
    print("Nhập ký tự bất kỳ để xem mã ASCII (Nhấn ESC để thoát):")
    while True:
        if msvcrt.kbhit():
            char = msvcrt.getch()
            ma_ascii = ord(char)
            if ma_ascii == 27:  
                print("\nĐã nhấn ESC. Kết thúc chương trình.")
                break
            print(f"Ký tự: {char.decode('utf-8', 'ignore')} - Mã ASCII: {ma_ascii}")

in_ma_ascii()