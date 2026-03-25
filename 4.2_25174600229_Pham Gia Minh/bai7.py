menu = {
    "1": "Cafe",
    "2": "Cam vat",
    "3": "Nuoc ep ca rot",
    "4": "Nuoc loc",
    "5": "Nuoc dua"
}

print("--- MENU ---")
for k, v in menu.items():
    print(f"{k}. {v}")

# WHILE
while True:
    chon = input("Chon do uong (1-5): ")
    if chon in menu:
        print(f"Ban da chon: {menu[chon]}")
        break
    else:
        print("Khong co trong menu, moi chon lai.")

# FOR 
found = False
for _ in iter(int, 1):
    if found: break
    chon_f = input("Nhap lai lua chon de kiem tra cach For: ")
    for k in menu:
        if chon_f == k:
            print(f"Cach For xac nhan: {menu[k]}")
            found = True
            break