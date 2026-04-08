#bai14
n = int(input("nhap so luong tuple: "))
danh_sach = []
for i in range(n):
    print(f"nhap tuple thu {i+1} (name, age, score):")
    name = input("  name: ")
    age = int(input("  age: "))
    score = int(input("  score: "))
    danh_sach.append((name, age, score))
danh_sach.sort(key=lambda x: (x[0], x[1], x[2]))
print("danh sach sau khi sap xep:")
for t in danh_sach:
    print(t)