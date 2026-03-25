menu = ["Cafe", "Cam vắt", "Nước ép cà rốt", "Nước lọc", "Nước dừa"]
print("---------- MENU ----------")
for i in range(len(menu)):
    print(f"{i + 1}. {menu[i]}")
lua_chon = int(input("Mời bạn nhập số thứ tự món (1-5): "))
da_chon = False
for i in range(len(menu)):
    if lua_chon == i + 1:
        print(f"Bạn đã chọn: {menu[i]}")
        da_chon = True
        break 
else:
    print("Lựa chọn không hợp lệ!")
