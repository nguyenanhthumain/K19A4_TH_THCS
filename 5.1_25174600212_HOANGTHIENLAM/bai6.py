
import random
lua_chon = ["keo", "bua", "bao"]
thang = 0
hoa = 0
thua = 0
for i in range(5):
    user = input("Nhập (keo/bua/bao): ")
    may = random.choice(lua_chon)
    print("Máy chọn:", may)

    if user == may:
        hoa += 1
    elif (user == "keo" and may == "bao") or \
         (user == "bua" and may == "keo") or \
         (user == "bao" and may == "bua"):
        thang += 1
    else:
        thua += 1
print("Thắng:", thang)
print("Hòa:", hoa)
print("Thua:", thua)