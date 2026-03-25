while True:
    x = float(input("Nhập số: "))
    # Nếu là số âm hoặc số thập phân thì dừng
    if x < 0 or x % 1 != 0:
        print("Kết thúc!")
        break
    print("Bạn nhập số nguyên dương:", int(x))