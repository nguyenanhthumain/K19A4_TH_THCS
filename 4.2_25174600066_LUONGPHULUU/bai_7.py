# Cách 1 while:
while True:
    print("===== MENU ĐỒ UỐNG =====")
    print("1. Cafe")
    print("2. Cam vắt")
    print("3. Nước ép cà rốt")
    print("4. Nước lọc")
    print("5. Nước dừa")
    chon = int(input("Nhập lựa chọn (1-5): "))
    match chon:
        case 1:
            print("Bạn chọn: Cafe")
            break
        case 2:
            print("Bạn chọn: Cam vắt")
            break
        case 3:
            print("Bạn chọn: Nước ép cà rốt")
            break
        case 4:
            print("Bạn chọn: Nước lọc")
            break
        case 5:
            print("Bạn chọn: Nước dừa")
            break
        case _:
            print("Sai! Nhập lại.\n")
# Cách 2 for:
menu = ["Cafe", "Cam vắt", "Nước ép cà rốt", "Nước lọc", "Nước dừa"]
print("===== MENU ĐỒ UỐNG =====")
stt = 1
for mon in menu:
    print(stt, ".", mon)
    stt += 1
chon = int(input("Nhập lựa chọn (1-5): "))
stt = 1
for mon in menu:
    if chon == stt:
        print("Bạn đã chọn:", mon)
        break
    stt += 1
else:
    print("Lựa chọn không hợp lệ!")