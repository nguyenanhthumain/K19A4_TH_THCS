#bai6
import random
lua_chon = ["bua", "keo", "la"]
thang = 0
hoa = 0
thua = 0
print("tro choi bua - keo - la")
print("co 5 luot choi\n")

for i in range(1, 6):
    print(f"luot {i}:")
    nguoi_choi = input(" chon (bua/keo/la): ").lower().strip()
    while nguoi_choi not in lua_chon:
        print("khong hop le, chi duoc chon: bua, keo, la")
        nguoi_choi = input(" chon (bua/keo/la): ").lower().strip()
    may = random.choice(lua_chon)
    print(f"may tinh chon: {may}")
    if nguoi_choi == may:
        print("hoa!")
        hoa += 1
    elif (nguoi_choi == "bua" and may == "keo") or \
         (nguoi_choi == "keo" and may == "la") or \
         (nguoi_choi == "la" and may == "bua"):
        print("thang!")
        thang += 1
    else:
        print("thua!")
        thua += 1
    print("-------------------")
print("\nket qua sau 5 luot:")
print("thang:", thang, "luot")
print("hoa:", hoa, "luot")
print("thua:", thua, "luot")