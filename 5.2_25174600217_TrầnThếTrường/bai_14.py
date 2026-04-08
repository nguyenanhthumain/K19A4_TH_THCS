n = int(input("Nhập số lượng bản ghi: "))
data = []

for i in range(n):
    entry = input(f"Nhập bản ghi {i+1} (name age score): ").split()
    name = entry[0]
    age = int(entry[1])
    score = int(entry[2])
    data.append((name, age, score))
data_sorted = sorted(data, key=lambda x: (x[0], x[1], x[2]))

print("\nDanh sách sau khi sắp xếp:")
for item in data_sorted:
    print(item)