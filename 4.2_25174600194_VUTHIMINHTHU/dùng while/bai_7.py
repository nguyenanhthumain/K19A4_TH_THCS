menu = ["Cafe", "Cam vắt", "Nước ép cà rốt", "Nước lọc", "Nước dừa"]
print("---------- MENU ----------")
for i in range(len(menu)):
    print(f"{i + 1}. {menu[i]}")
while True:
    lua_chon = input("Mời bạn nhập số thứ tự món (1-5): ")
    if lua_chon == '1':
        print(">> Bạn đã chọn: Cafe")
    elif lua_chon == '2':
        print(">> Bạn đã chọn: Cam vắt")
    elif lua_chon == '3':
        print(">> Bạn đã chọn: Nước ép cà rốt")
    elif lua_chon == '4':
        print(">> Bạn đã chọn: Nước lọc")
    elif lua_chon == '5':
        print(">> Bạn đã chọn: Nước dừa")
    else:
        print("Yêu cầu nhập lại")