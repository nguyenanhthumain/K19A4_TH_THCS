"""Bài 5: Viết hàm nhập ký tự bất kỳ từ bàn phím, in ra màn hình giá trị ASCII của
ký tự đó, vòng lặp chỉ kết thúc khi nhấn phím ESC."""

import msvcrt

def ascii_value():
    print("--- Chương trình in giá trị ASCII ---")
    print("Nhấn một phím bất kỳ để xem mã ASCII (Nhấn ESC để thoát)")
    
    while True:
        if msvcrt.kbhit():
            char_raw = msvcrt.getch()
            
            ma_ascii = ord(char_raw)
            
            if ma_ascii == 27:
                print("\nĐã nhấn ESC. Thoát chương trình.")
                break
            
            try:
                char_hien_thi = char_raw.decode('utf-8')
                print(f"Ký tự: '{char_hien_thi}' - Mã ASCII: {ma_ascii}")
            except:
                print(f"Phím chức năng - Mã ASCII: {ma_ascii}")

if __name__ == "__main__":
    ascii_value()
