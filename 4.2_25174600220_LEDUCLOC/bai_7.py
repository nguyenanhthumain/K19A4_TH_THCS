#While
menu = ["Cafe", "Cam vắt", "Nước ép cà rốt", "Nước lọc", "Nước dừa"]
print("--- MENU ---")
for i, mon in enumerate(menu, 1):
    print(f"{i}. {mon}")

lua_chon = 0
while lua_chon < 1 or lua_chon > 5:
    lua_chon = int(input("Mời bạn chọn món (1-5): "))
    if 1 <= lua_chon <= 5:
        print(f"Bạn đã gọi: {menu[lua_chon-1]}")
    else:
        print("Món không có trong menu, hãy chọn lại!")

#FOR
for lan_thu in range(3):
    lua_chon = int(input("Mời bạn chọn món (1-5): "))
    if 1 <= lua_chon <= 5:
        print(f"Bạn đã gọi: {menu[lua_chon-1]}")
        break
    else:
        print(f"Sai rồi! Bạn còn {2 - lan_thu} lần chọn lại.")