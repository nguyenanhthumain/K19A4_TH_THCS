n = int(input("Nhập số lượng người: "))
data = []
for i in range(n):
    name = input(f"Nhập tên người thứ {i+1}: ")
    age = int(input(f"Nhập tuổi của {name}: "))
    score = float(input(f"Nhập điểm của {name}: "))
    data.append((name, age, score))
du_lieu = sorted(data, key=lambda x: (x[0], x[1], x[2]))
print("a.Sắp xếp theo name -> age -> score:")
for item in du_lieu:
    print(item)
sorted_priority = sorted(data, key=lambda x: (x[0], x[1], x[2]))
print("b.Ưu tiên tên > tuổi > điểm:")
for item in sorted_priority:
    print(item)