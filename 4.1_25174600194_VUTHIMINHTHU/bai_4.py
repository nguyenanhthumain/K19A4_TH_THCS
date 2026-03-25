n = int(input("Nhập giá trị dương:"))
for i in range(n):
    m = float(input(f"Nhập số thứ {i+1}:"))
    if m<0:
        print(f"Chương trình kết thúc, đã phát hiện số âm")
