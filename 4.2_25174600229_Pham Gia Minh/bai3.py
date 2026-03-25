print("Chuong trinh se dung neu ban nhap so am hoac so thap phan.")

# While 
print("--- TEST VOI WHILE ---")
while True:
    du_lieu = input("Nhap mot so bat ky: ")
    if '.' in du_lieu:
        print("Day la so thap phan. Dung chuong trinh!")
        break
    val = float(du_lieu)
    if val < 0:
        print("Day la so am. Dung chuong trinh!")
        break

# For 
print("--- TEST VOI FOR ---")
for _ in iter(int, 1):
    du_lieu = input("Nhap tiep de kiem tra For: ")
    if '.' in du_lieu or float(du_lieu) < 0:
        break