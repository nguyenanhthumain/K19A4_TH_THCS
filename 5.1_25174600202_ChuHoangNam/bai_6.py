#cau6
thang = 0
hoa = 0
thua = 0
for luot in range(1, 6):
    print(f"\nLuot choi thu{luot}")
    nguoi_chon = input("Nhap keo,bua hoac la: ")
    so_may_man = int(input("nhap 1 so bat ki de may chon: "))    
    lua_chon_may = ["keo", "bua", "la"]
    may_chon = lua_chon_may[so_may_man % 3]
    print(f"may chon: {may_chon}")
    if nguoi_chon == may_chon:
        print("Hoa")
        hoa += 1
    elif (nguoi_chon == "Bua" and may_chon == "keo") or \
         (nguoi_chon == "Keo" and may_chon == "la") or \
         (nguoi_chon == "la" and may_chon == "bua"):
        print("ban thang")
        thang += 1
    else:
        print("may thang")
        thua += 1

print("-" * 20)
print(f"Ket qua sau 5 luot: Thang {thang}, Hoa {hoa}, Thua {thua}")