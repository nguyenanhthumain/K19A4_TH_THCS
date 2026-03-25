menu = ["Cafe", "Cam vắt", "Cà rốt", "Nước lọc", "Nước dừa"]
for i in range(len(menu)):
    print(f"{i+1}. {menu[i]}")
chon = int(input("Chọn món: "))
print(f"Bạn đã chọn {menu[chon-1]}")
#
menu = ["Cafe", "Cam vắt", "Cà rốt", "Nước lọc", "Nước dừa"]
i = 0
while i < len(menu):
    print(f"{i+1}. {menu[i]}")
    i += 1
chon = int(input("Chọn món: "))
print(f"Bạn đã chọn {menu[chon-1]}")