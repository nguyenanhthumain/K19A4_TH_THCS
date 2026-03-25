print("Menu:")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")

chon = int(input("Chọn đồ uống (1-5): "))

while chon < 1 or chon > 5:
    chon = int(input("Chọn số từ 1 tới 5: "))

if chon == 1:
    print("Cafe")
elif chon == 2:
    print("Cam vắt")
elif chon == 3:
    print("Nước ép cà rốt")
elif chon == 4:
    print("Nước lọc")
else:
    print("Nước dừa")
    
    
    
    
    
    

print("Menu:")
print("1. Cafe")
print("2. Cam vắt")
print("3. Nước ép cà rốt")
print("4. Nước lọc")
print("5. Nước dừa")

for _ in range(100):
    chon = int(input("Chọn đồ uống (1-5): "))
    if 1 <= chon <= 5:
        break
    print("Chọn số từ 1 tới 5: ")

if chon == 1:
    print("Cafe")
elif chon == 2:
    print("Cam vắt")
elif chon == 3:
    print("Nước ép cà rốt")
elif chon == 4:
    print("Nước lọc")
else:
    print("Nước dừa")