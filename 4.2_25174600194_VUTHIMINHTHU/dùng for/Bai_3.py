for i in iter(int, 1):
    n = input("Nhập giá trị:")
    if "." in n:
        print(f"Phát hiện lỗi dừng chương trình")
        break
else:
    print(f"Giá trị hợp lệ")