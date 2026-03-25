menu = ["Cafe", "Cam vắt", "Nước ép cà rốt", "Nước lọc", "Nước dừa"]

print("C1:FOR")
for i in range(len(menu)):
    print(f"{i + 1}. {menu[i]}")
for _ in range(10):
    chon_for = int(input("\nChọn đồ uống (1-5): "))
    if 1 <= chon_for <= 5:
        print(f"-> Bạn đã gọi: {menu[chon_for - 1]}")
        break
    print("Lựa chọn không hợp lệ!")


print("C2:WhILE")
i = 0
while i < len(menu):
    print(f"{i + 1}. {menu[i]}")
    i += 1
while True:
    chon_while = int(input("\nChọn đồ uống (1-5): "))
    if 1 <= chon_while <= 5:
        print(f"-> Bạn đã gọi: {menu[chon_while - 1]}")
        break
    print("Lựa chọn không hợp lệ!")